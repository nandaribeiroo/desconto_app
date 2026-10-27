
from src.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class PedidoPresenter:
    """Formata os resultados dos casos de uso para apresentação."""

    def apresentar(self, output_dto: CriarPedidoOutputDTO) -> dict:
        return {
            "cliente": output_dto.cliente,
            "valor_original": output_dto.valor_original,
            "valor_desconto": output_dto.valor_desconto,
            "valor_final": output_dto.valor_final,
            "tipo_desconto": output_dto.tipo_desconto,
        }

    def apresentar_lista(
        self, output_dtos: list[CriarPedidoOutputDTO]
    ) -> list[dict]:
        return [
            self.apresentar(output_dto)
            for output_dto in output_dtos
        ]
