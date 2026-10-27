
from src.models.desconto import Desconto


class Pedido:
    """Representa um pedido e suas regras de negócio."""

    def __init__(self, cliente: str, desconto: Desconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0

    def valor_final(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)
