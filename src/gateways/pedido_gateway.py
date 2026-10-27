
from abc import ABC, abstractmethod
from src.models.pedido import Pedido


class PedidoGateway(ABC):
    """Define o contrato para salvar e listar pedidos."""

    @abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def listar_todos(self) -> list[dict]:
        pass
