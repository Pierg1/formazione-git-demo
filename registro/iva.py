"""Calcolo dell'IVA e degli imponibili."""

from decimal import Decimal, ROUND_HALF_UP

ALIQUOTE = {
    "ordinaria": Decimal("22"),
    "ridotta": Decimal("10"),
    "minima": Decimal("4"),
}


def arrotonda(importo):
    """Arrotonda a due decimali con il criterio commerciale."""
    return Decimal(importo).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def imposta(imponibile, aliquota="ordinaria"):
    """Restituisce l'imposta calcolata sull'imponibile."""
    percentuale = ALIQUOTE[aliquota]
    return arrotonda(Decimal(imponibile) * percentuale / Decimal("100"))


def totale(imponibile, aliquota="ordinaria"):
    """Restituisce il totale documento, imponibile piu' imposta."""
    return arrotonda(Decimal(imponibile) + imposta(imponibile, aliquota))
