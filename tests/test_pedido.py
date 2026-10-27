
import pytest

from src.models.desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium,
)
from src.models.pedido import Pedido


@pytest.mark.parametrize(
    ("classe_desconto", "valor", "valor_esperado"),
    [
        (DescontoNormal, 100, 90),
        (DescontoVIP, 100, 80),
        (DescontoPremium, 100, 70),
    ],
)
def test_valor_final_do_pedido(
    classe_desconto,
    valor,
    valor_esperado,
):
    pedido = Pedido("Cliente Teste", classe_desconto())

    resultado = pedido.valor_final(valor)

    assert resultado == valor_esperado
