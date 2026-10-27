
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parents[2] / "data" / "pedidos.db"


def conectar():
    """Abre uma conexão com o banco de dados SQLite."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    """Cria a tabela de pedidos caso ainda não exista."""
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                valor_original REAL NOT NULL,
                percentual_desconto REAL NOT NULL,
                valor_final REAL NOT NULL
            )
        """)
