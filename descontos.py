
class SemDesconto:
    pass


class DescontoPercentual:
    def __init__(self, percentual):
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual deve estar entre 0 e 100.")
        self.percentual = percentual


class DescontoFixo:
    def __init__(self, valor):
        if valor < 0:
            raise ValueError("O desconto fixo não pode ser negativo.")
        self.valor = valor


class CalculadoraDePreco:
    def __init__(self, estrategia):
        if not isinstance(
            estrategia,
            (SemDesconto, DescontoPercentual, DescontoFixo)
        ):
            raise TypeError("A estratégia de desconto é inválida.")

        self.estrategia = estrategia

    def calcular(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        if isinstance(self.estrategia, SemDesconto):
            return round(preco, 2)

        elif isinstance(self.estrategia, DescontoPercentual):
            percentual = self.estrategia.percentual
            return round(preco * (1 - percentual / 100), 2)

        elif isinstance(self.estrategia, DescontoFixo):
            valor = self.estrategia.valor
            return round(max(0, preco - valor), 2)
