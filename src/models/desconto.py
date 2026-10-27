from abc import ABC, abstractmethod


class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoNormal(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2


class DescontoPremium(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3