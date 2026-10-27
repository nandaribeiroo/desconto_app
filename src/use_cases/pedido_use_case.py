
from src.models.pedido import Pedido
from src.models.desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium,
)
from src.gateways.pedido_gateway import PedidoGateway
from src.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class CriarPedido:
    def __init__(self, pedido_gateway: PedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(
        self, input_dto: CriarPedidoInputDTO
    ) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()

        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(input_dto.cliente, desconto)
        pedido.valor_original = input_dto.valor_original

        self.pedido_gateway.salvar(pedido)

        valor_desconto = desconto.calcular(input_dto.valor_original)
        valor_final = pedido.valor_final(input_dto.valor_original)

        return CriarPedidoOutputDTO(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            valor_desconto=valor_desconto,
            valor_final=valor_final,
            tipo_desconto=tipo_desconto,
        )

    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        pedidos = self.pedido_gateway.listar_todos()
        lista_dto = []

        for pedido in pedidos:
            if isinstance(pedido.desconto, DescontoNormal):
                tipo_desconto = "normal"
            elif isinstance(pedido.desconto, DescontoVIP):
                tipo_desconto = "vip"
            elif isinstance(pedido.desconto, DescontoPremium):
                tipo_desconto = "premium"
            else:
                raise ValueError("Tipo de desconto inválido")

            valor_desconto = pedido.desconto.calcular(
                pedido.valor_original
            )

            lista_dto.append(
                CriarPedidoOutputDTO(
                    cliente=pedido.cliente,
                    valor_original=pedido.valor_original,
                    valor_desconto=valor_desconto,
                    valor_final=pedido.valor_final(pedido.valor_original),
                    tipo_desconto=tipo_desconto,
                )
            )

        return lista_dto
