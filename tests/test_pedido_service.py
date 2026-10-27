
from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService


class PedidoRepositoryStub:
    """Simula o repositório sem acessar o banco de dados."""

    def __init__(self):
        self.pedidos = []

    def salvar(self, pedido):
        self.pedidos.append({
            "id": len(self.pedidos) + 1,
            "cliente": pedido.cliente,
            "valor_original": pedido.valor_original,
            "percentual_desconto": 20,
            "valor_final": pedido.valor_final(
                pedido.valor_original
            ),
        })

    def listar_todos(self):
        return self.pedidos


def test_adicionar_pedido():
    repository = PedidoRepositoryStub()
    service = PedidoService(repository)

    pedido = Pedido("Maria", DescontoVIP())
    pedido.valor_original = 100

    service.adicionar_pedido(pedido)

    pedidos = service.listar_pedidos()

    assert len(pedidos) == 1
    assert pedidos[0]["cliente"] == "Maria"
    assert pedidos[0]["valor_final"] == 80
