"""Registro delle fatture emesse."""

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from registro.iva import arrotonda, imposta, totale


@dataclass
class Riga:
    descrizione: str
    quantita: int
    prezzo_unitario: Decimal
    aliquota: str = "ordinaria"
    sconto: Decimal = Decimal("0")

    @property
    def lordo(self):
        return arrotonda(Decimal(self.quantita) * Decimal(self.prezzo_unitario))

    @property
    def imponibile(self):
        riduzione = self.lordo * Decimal(self.sconto) / Decimal("100")
        return arrotonda(self.lordo - riduzione)


@dataclass
class Fattura:
    numero: str
    data: date
    cliente: str
    righe: list = field(default_factory=list)

    def aggiungi_riga(self, descrizione, quantita, prezzo_unitario, aliquota="ordinaria", sconto=0):
        self.righe.append(
            Riga(descrizione, quantita, Decimal(prezzo_unitario), aliquota, Decimal(sconto))
        )
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


class Registro:
    """Raccolta delle fatture di un esercizio."""

    def __init__(self):
        self._fatture = []

    def aggiungi(self, fattura):
        if self.trova(fattura.numero) is not None:
            raise ValueError("Numero fattura gia' presente: %s" % fattura.numero)
        self._fatture.append(fattura)
        return fattura

    def trova(self, numero):
        for f in self._fatture:
            if f.numero == numero:
                return f
        return None

    def per_cliente(self, cliente):
        return [f for f in self._fatture if f.cliente == cliente]

    def totale_imponibile(self):
        return arrotonda(sum((f.imponibile for f in self._fatture), Decimal("0")))

    def totale_imposta(self):
        return arrotonda(sum((f.imposta for f in self._fatture), Decimal("0")))

    def __len__(self):
        return len(self._fatture)

    def __iter__(self):
        return iter(self._fatture)
