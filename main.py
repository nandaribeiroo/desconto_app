
from src.controllers.pedido_controller import PedidoController
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium


def cadastrar_exemplos(controller):
    controller.criar_pedido("Ana", 100, DescontoNormal())
    controller.criar_pedido("Bruno", 200, DescontoVIP())
    controller.criar_pedido("Carla", 300, DescontoPremium())


def listar_pedidos(controller):
    print("Pedidos cadastrados:")

    for pedido in controller.listar_pedidos():
        print(
            f"ID: {pedido['id']} | "
            f"Cliente: {pedido['cliente']} | "
            f"Valor original: R$ {pedido['valor_original']:.2f} | "
            f"Desconto: {pedido['percentual_desconto']:.0f}% | "
            f"Valor final: R$ {pedido['valor_final']:.2f}"
        )


if __name__ == "__main__":
    controller = PedidoController()

    opcao = input(
        "Escolha uma opção:\n"
        "1 - Cadastrar pedidos de exemplo\n"
        "2 - Listar pedidos cadastrados\n"
        "Opção: "
    )

    if opcao == "1":
        cadastrar_exemplos(controller)
        print("Pedidos de exemplo cadastrados com sucesso.")
    elif opcao == "2":
        listar_pedidos(controller)
    else:
        print("Opção inválida.")
