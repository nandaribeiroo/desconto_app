
from src.controllers.pedido_controller import PedidoController
from src.use_cases.pedido_use_case import CriarPedido
from src.gateways.pedido_gateway import PedidoGateway
from src.models.pedido import Pedido
from src.presenters.pedido_presenter import PedidoPresenter


class PedidoGatewayStub(PedidoGateway):
    """Simula o Gateway para os testes."""

    def __init__(self):
        self.pedidos = []

    def salvar(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def listar_todos(self) -> list[Pedido]:
        return self.pedidos


def test_criar_pedido():
    gateway = PedidoGatewayStub()
    use_case = CriarPedido(gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(use_case, presenter)

    resultado = controller.criar("Maria", 100, "vip")

    assert resultado["cliente"] == "Maria"
    assert resultado["valor_original"] == 100
    assert resultado["valor_desconto"] == 20
    assert resultado["valor_final"] == 80
    assert len(gateway.pedidos) == 1


def test_listar_pedidos():
    gateway = PedidoGatewayStub()
    use_case = CriarPedido(gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(use_case, presenter)

    controller.criar("Maria", 100, "vip")
    pedidos = controller.listar()

    assert len(pedidos) == 1
    assert pedidos[0]["cliente"] == "Maria"
    assert pedidos[0]["valor_final"] == 80
