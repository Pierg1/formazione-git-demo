"""Calcolo dell'IVA e degli imponibili."""

from decimal import Decimal

ALIQUOTE = {
    "ordinaria": Decimal("22"),
    "ridotta": Decimal("10"),
    "minima": Decimal("4"),
}


def imposta(imponibile, aliquota="ordinaria"):
    """Restituisce l'imposta calcolata sull'imponibile."""
    percentuale = ALIQUOTE[aliquota]
    return Decimal(imponibile) * percentuale / Decimal("100")


def totale(imponibile, aliquota="ordinaria"):
    """Restituisce il totale documento, imponibile piu' imposta."""
    return Decimal(imponibile) + imposta(imponibile, aliquota)
