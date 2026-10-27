
from src.use_cases.pedido_use_case import CriarPedido
from src.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.presenters.pedido_presenter import PedidoPresenter


class PedidoController:
    """Recebe as entradas e encaminha os resultados para o Presenter."""

    def __init__(
        self,
        criar_pedido_use_case: CriarPedido,
        presenter: PedidoPresenter,
    ):
        self.criar_pedido_use_case = criar_pedido_use_case
        self.presenter = presenter

    def criar(
        self,
        cliente: str,
        valor_original: float,
        tipo_desconto: str,
    ) -> dict:
        input_dto = CriarPedidoInputDTO(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto,
        )

        output_dto = self.criar_pedido_use_case.executar(input_dto)
        return self.presenter.apresentar(output_dto)

    def listar(self) -> list[dict]:
        output_dtos = self.criar_pedido_use_case.listar_pedidos()
        return self.presenter.apresentar_lista(output_dtos)
