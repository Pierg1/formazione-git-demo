"""Registro delle fatture emesse."""

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from registro.iva import arrotonda, imposta


@dataclass
class Riga:
    descrizione: str
    quantita: int
    prezzo_unitario: Decimal
    aliquota: str = "ordinaria"

    @property
    def imponibile(self):
        return arrotonda(Decimal(self.quantita) * Decimal(self.prezzo_unitario))


@dataclass
class Fattura:
    numero: str
    data: date
    cliente: str
    righe: list = field(default_factory=list)

    def aggiungi_riga(self, descrizione, quantita, prezzo_unitario, aliquota="ordinaria"):
        self.righe.append(Riga(descrizione, quantita, Decimal(prezzo_unitario), aliquota))
        return self

    @property
    def imponibile(self):
        return arrotonda(sum((r.imponibile for r in self.righe), Decimal("0")))

    @property
    def imposta(self):
        return arrotonda(sum((imposta(r.imponibile, r.aliquota) for r in self.righe), Decimal("0")))

    @property
    def totale(self):
        return arrotonda(self.imponibile + self.imposta)
