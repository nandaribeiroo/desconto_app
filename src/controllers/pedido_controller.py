
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService


class PedidoController:
    """Recebe solicitações e encaminha ao serviço de pedidos."""

    def __init__(self, service=None):
        self.service = service or PedidoService()

    def criar_pedido(
        self,
        cliente: str,
        valor: float,
        desconto,
    ) -> None:
        pedido = Pedido(cliente, desconto)
        pedido.valor_original = valor

        self.service.adicionar_pedido(pedido)

    def listar_pedidos(self) -> list[dict]:
        return self.service.listar_pedidos()
