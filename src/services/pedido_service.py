
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository


class PedidoService:
    """Processa pedidos e consulta os dados armazenados."""

    def __init__(self, repository=None):
        self.repository = repository or PedidoRepository()

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.repository.salvar(pedido)

    def processar_pedidos(self) -> None:
        for pedido in self.repository.listar_todos():
            print(f"Cliente: {pedido['cliente']}")
            print(f"Valor final: R$ {pedido['valor_final']:.2f}")

    def listar_pedidos(self) -> list[dict]:
        return self.repository.listar_todos()
