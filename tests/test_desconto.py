
import pytest

from src.models.desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium,
)


@pytest.mark.parametrize(
    ("classe_desconto", "valor", "desconto_esperado"),
    [
        (DescontoNormal, 100, 10),
        (DescontoVIP, 100, 20),
        (DescontoPremium, 100, 30),
    ],
)
def test_calcular_desconto(
    classe_desconto,
    valor,
    desconto_esperado,
):
    desconto = classe_desconto()

    assert desconto.calcular(valor) == desconto_esperado
