
from abc import ABC, abstractmethod


class EstrategiaDesconto(ABC):
    @abstractmethod
    def aplicar(self, preco):
        pass


class SemDesconto(EstrategiaDesconto):
    def aplicar(self, preco):
        return round(preco, 2)


class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, percentual):
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual deve estar entre 0 e 100.")
        self.percentual = percentual

    def aplicar(self, preco):
        return round(preco * (1 - self.percentual / 100), 2)


class DescontoFixo(EstrategiaDesconto):
    def __init__(self, valor):
        if valor < 0:
            raise ValueError("O desconto fixo não pode ser negativo.")
        self.valor = valor

    def aplicar(self, preco):
        return round(max(0, preco - self.valor), 2)


class CalculadoraDePreco:
    def __init__(self, estrategia):
        if not isinstance(estrategia, EstrategiaDesconto):
            raise TypeError("A estratégia de desconto é inválida.")
        self.estrategia = estrategia

    def calcular(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        return self.estrategia.aplicar(preco)
