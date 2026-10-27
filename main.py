
from src.frameworks.database.memory_database import MemoryDatabase
from src.adapters.repositories.memory_pedido_repository import (
    MemoryPedidoRepository,
)
from src.use_cases.pedido_use_case import CriarPedido
from src.controllers.pedido_controller import PedidoController
from src.presenters.pedido_presenter import PedidoPresenter


def main():
    database = MemoryDatabase()
    gateway = MemoryPedidoRepository(database)

    criar_pedido = CriarPedido(gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido, presenter)

    resultado = controller.criar("Ana", 100.0, "normal")

    print("Pedido criado:")
    print(f"Cliente: {resultado['cliente']}")
    print(f"Valor original: R$ {resultado['valor_original']:.2f}")
    print(f"Desconto: R$ {resultado['valor_desconto']:.2f}")
    print(f"Valor final: R$ {resultado['valor_final']:.2f}")

    print("\nPedidos cadastrados:")
    for pedido in controller.listar():
        print(
            f"{pedido['cliente']}: "
            f"R$ {pedido['valor_final']:.2f}"
        )


if __name__ == "__main__":
    main()
