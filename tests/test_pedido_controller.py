
from src.controllers.pedido_controller import PedidoController
from src.use_cases.pedido_use_case import CriarPedido
from src.gateways.pedido_gateway import PedidoGateway
from src.models.pedido import Pedido


class PedidoGatewayStub(PedidoGateway):
    """Simula o Gateway para testar o fluxo sem banco de dados."""

    def __init__(self):
        self.pedidos = []

    def salvar(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def listar_todos(self) -> list[Pedido]:
        return self.pedidos


def test_criar_pedido():
    gateway = PedidoGatewayStub()
    use_case = CriarPedido(gateway)
    controller = PedidoController(use_case)

    pedido = controller.criar("Maria", 100, "vip")

    assert pedido.cliente == "Maria"
    assert pedido.valor_original == 100
    assert len(gateway.pedidos) == 1


def test_listar_pedidos():
    gateway = PedidoGatewayStub()
    use_case = CriarPedido(gateway)
    controller = PedidoController(use_case)

    controller.criar("Maria", 100, "vip")

    pedidos = controller.listar()

    assert len(pedidos) == 1
    assert pedidos[0].cliente == "Maria"
