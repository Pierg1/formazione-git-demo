from datetime import date
from decimal import Decimal

import pytest

from registro.fatture import Fattura, Registro


def fattura_di_prova(numero="2026/001", cliente="Studio Bianchi"):
    f = Fattura(numero, date(2026, 1, 15), cliente)
    f.aggiungi_riga("Canone gestionale", 12, "85.00")
    return f


def test_imponibile_di_una_riga():
    assert fattura_di_prova().imponibile == Decimal("1020.00")


def test_totale_con_aliquota_ordinaria():
    assert fattura_di_prova().totale == Decimal("1244.40")


def test_numero_duplicato_non_ammesso():
    r = Registro()
    r.aggiungi(fattura_di_prova())
    with pytest.raises(ValueError):
        r.aggiungi(fattura_di_prova())


def test_ricerca_per_cliente():
    r = Registro()
    r.aggiungi(fattura_di_prova("2026/001", "Studio Bianchi"))
    r.aggiungi(fattura_di_prova("2026/002", "Studio Verdi"))
    assert len(r.per_cliente("Studio Bianchi")) == 1
