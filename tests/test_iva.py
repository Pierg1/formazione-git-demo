from decimal import Decimal

from registro.iva import imposta, totale


def test_imposta_ordinaria():
    assert imposta("100.00") == Decimal("22.00")


def test_imposta_ridotta():
    assert imposta("100.00", "ridotta") == Decimal("10.00")


def test_totale_somma_imponibile_e_imposta():
    assert totale("100.00") == Decimal("122.00")


def test_arrotondamento_commerciale():
    assert imposta("0.57") == Decimal("0.13")
