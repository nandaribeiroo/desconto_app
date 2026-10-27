
from src.frameworks.database.memory_database import MemoryDatabase
from src.adapters.repositories.memory_pedido_repository import (
    MemoryPedidoRepository,
)
from src.use_cases.pedido_use_case import CriarPedido
from src.controllers.pedido_controller import PedidoController


def main():
    database = MemoryDatabase()
    gateway = MemoryPedidoRepository(database)
    criar_pedido = CriarPedido(gateway)
    controller = PedidoController(criar_pedido)

    pedido = controller.criar("Ana", 100.0, "normal")

    print(f"Cliente: {pedido.cliente}")
    print(f"Valor original: R$ {pedido.valor_original:.2f}")
    print(f"Valor final: R$ {pedido.valor_final(pedido.valor_original):.2f}")

    print("\nPedidos cadastrados:")
    for pedido in controller.listar():
        print(f"{pedido.cliente}: R$ {pedido.valor_final(pedido.valor_original):.2f}")


if __name__ == "__main__":
    main()
