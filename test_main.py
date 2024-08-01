import pytest

from main import ContaBanco

@pytest.fixture

def conta():
    return ContaBanco("Valker" , 100)

def test_depositar(conta):
    assert conta.depositar(20) == 120
    #assert conta.saldo_em_conta() == 20

def test_sacar(conta):
    assert conta.sacar(10) == 90

def test_saldo_em_conta(conta):
    assert conta.saldo_em_conta() == 100

def test_titular(conta):
    assert conta.titular() == "Valker"    