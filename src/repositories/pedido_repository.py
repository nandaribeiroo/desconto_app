
from src.database.database import conectar
from src.database.database import criar_tabela
from src.models.pedido import Pedido


class PedidoRepository:
    """Responsável por salvar e consultar pedidos no SQLite."""

    def __init__(self):
        criar_tabela()

    def salvar(self, pedido: Pedido) -> None:
        valor_original = pedido.valor_original
        valor_desconto = pedido.desconto.calcular(valor_original)
        valor_final = valor_original - valor_desconto

        if isinstance(pedido.desconto, type(None)):
            raise ValueError("O pedido precisa ter um desconto válido.")

        percentual_desconto = (
            valor_desconto / valor_original * 100
            if valor_original > 0
            else 0
        )

        with conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO pedidos
                (cliente, valor_original, percentual_desconto, valor_final)
                VALUES (?, ?, ?, ?)
                """,
                (
                    pedido.cliente,
                    valor_original,
                    percentual_desconto,
                    valor_final,
                ),
            )

    def listar_todos(self) -> list[dict]:
        with conectar() as conexao:
            linhas = conexao.execute(
                """
                SELECT id, cliente, valor_original,
                       percentual_desconto, valor_final
                FROM pedidos
                ORDER BY id
                """
            ).fetchall()

        return [
            {
                "id": linha[0],
                "cliente": linha[1],
                "valor_original": linha[2],
                "percentual_desconto": linha[3],
                "valor_final": linha[4],
            }
            for linha in linhas
        ]
