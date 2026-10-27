
from src.controllers.pedido_controller import PedidoController
from src.models.desconto import DescontoVIP


class PedidoServiceStub:
    """Simula o serviço sem acessar o banco de dados."""

    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.pedidos


def test_criar_pedido():
    service = PedidoServiceStub()
    controller = PedidoController(service)

    controller.criar_pedido("Maria", 100, DescontoVIP())

    assert len(service.pedidos) == 1
    assert service.pedidos[0].cliente == "Maria"
    assert service.pedidos[0].valor_original == 100


def test_listar_pedidos():
    service = PedidoServiceStub()
    controller = PedidoController(service)

    resultado = [{"id": 1, "cliente": "Maria", "valor_final": 80}]

    service.listar_pedidos = lambda: resultado

    assert controller.listar_pedidos() == resultado
