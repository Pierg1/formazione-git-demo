from decimal import Decimal

import pytest

from registro.iva import imposta, totale, arrotonda


def test_imposta_ordinaria():
    assert imposta("100.00") == Decimal("22.00")


def test_imposta_ridotta():
    assert imposta("100.00", "ridotta") == Decimal("10.00")


def test_imposta_esente():
    assert imposta("100.00", "esente") == Decimal("0.00")


def test_totale_somma_imponibile_e_imposta():
    assert totale("100.00") == Decimal("122.00")


def test_aliquota_sconosciuta():
    with pytest.raises(ValueError):
        imposta("100.00", "agevolata")


def test_arrotondamento_commerciale():
    assert arrotonda("0.125") == Decimal("0.13")
