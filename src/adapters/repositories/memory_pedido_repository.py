
from src.models.pedido import Pedido
from src.gateways.pedido_gateway import PedidoGateway
from src.frameworks.database.memory_database import MemoryDatabase


class MemoryPedidoRepository(PedidoGateway):
    """Implementa o gateway de pedidos usando memória."""

    def __init__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido) -> None:
        self.database.pedidos.append(pedido)

    def listar_todos(self) -> list[Pedido]:
        return self.database.pedidos
