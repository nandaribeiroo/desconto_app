
from src.models.pedido import Pedido
from src.models.desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium,
)
from src.gateways.pedido_gateway import PedidoGateway


class CriarPedido:
    def __init__(self, pedido_gateway: PedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(
        self,
        cliente: str,
        valor_original: float,
        tipo_desconto: str,
    ) -> Pedido:
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, desconto)
        pedido.valor_original = valor_original
        self.pedido_gateway.salvar(pedido)

        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        return self.pedido_gateway.listar_todos()
