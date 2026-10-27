
from src.use_cases.pedido_use_case import CriarPedido


class PedidoController:
    """Recebe entradas e encaminha ao Use Case."""

    def __init__(self, criar_pedido: CriarPedido):
        self.criar_pedido_use_case = criar_pedido

    def criar(
        self,
        cliente: str,
        valor_original: float,
        tipo_desconto: str,
    ):
        return self.criar_pedido_use_case.executar(
            cliente,
            valor_original,
            tipo_desconto,
        )

    def listar(self):
        return self.criar_pedido_use_case.listar_pedidos()
