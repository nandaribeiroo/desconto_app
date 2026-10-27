
from src.gateways.pedido_gateway import PedidoGateway
from src.models.pedido import Pedido


class PedidoUseCase:
    """Coordena as operações de negócio relacionadas aos pedidos."""

    def __init__(self, gateway: PedidoGateway):
        self.gateway = gateway

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.gateway.salvar(pedido)

    def listar_pedidos(self) -> list[dict]:
        return self.gateway.listar_todos()
