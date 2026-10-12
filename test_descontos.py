
import pytest

from descontos import (
    CalculadoraDePreco,
    SemDesconto,
    DescontoPercentual,
    DescontoFixo,
)


# Casos planejados:
# 1. Calcular o preço sem desconto.
# 2. Aplicar desconto percentual.
# 3. Aplicar desconto fixo.
# 4. Impedir preço negativo.
# 5. Impedir percentual inválido.
# 6. Impedir desconto fixo negativo.
#
# Padrão escolhido: Strategy.
# Motivo: permitir trocar a regra de desconto sem alterar
# a calculadora.
#
# Tempo: preencher ao concluir cada fase.
# Uso de IA: apoio na criação dos testes e na organização do TDD.


def test_preco_sem_desconto():
    calculadora = CalculadoraDePreco(SemDesconto())
    assert calculadora.calcular(100) == 100


def test_desconto_percentual():
    calculadora = CalculadoraDePreco(DescontoPercentual(10))
    assert calculadora.calcular(100) == 90


def test_desconto_fixo():
    calculadora = CalculadoraDePreco(DescontoFixo(15))
    assert calculadora.calcular(100) == 85


def test_desconto_fixo_nao_deixa_preco_negativo():
    calculadora = CalculadoraDePreco(DescontoFixo(150))
    assert calculadora.calcular(100) == 0


@pytest.mark.parametrize("preco", [-1, -100])
def test_rejeita_preco_negativo(preco):
    calculadora = CalculadoraDePreco(SemDesconto())
    with pytest.raises(ValueError):
        calculadora.calcular(preco)


@pytest.mark.parametrize("percentual", [-1, 101])
def test_rejeita_percentual_invalido(percentual):
    with pytest.raises(ValueError):
        DescontoPercentual(percentual)


def test_rejeita_desconto_fixo_negativo():
    with pytest.raises(ValueError):
        DescontoFixo(-1)


def test_rejeita_estrategia_invalida():
    with pytest.raises(TypeError):
        CalculadoraDePreco("desconto inválido")
