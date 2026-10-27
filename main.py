
from src.controllers.pedido_controller import PedidoController
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.models.desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium,
)


def main():
    repository = PedidoRepository()
    service = PedidoService(repository)
    controller = PedidoController(service)

    controller.criar_pedido("Ana", 100.0, DescontoNormal())
    controller.criar_pedido("Bruno", 200.0, DescontoVIP())
    controller.criar_pedido("Carla", 300.0, DescontoPremium())

    service.processar_pedidos()


if __name__ == "__main__":
    main()
