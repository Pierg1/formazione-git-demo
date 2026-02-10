"""Esempio d'uso del registro. Si esegue con: python3 esempio.py"""

from datetime import date

from registro.fatture import Fattura, Registro
from registro.report import riepilogo_fattura, riepilogo_registro


def registro_di_esempio():
    r = Registro()

    f1 = Fattura("2026/001", date(2026, 1, 15), "Studio Bianchi")
    f1.aggiungi_riga("Canone gestionale", 12, "85.00")
    f1.aggiungi_riga("Assistenza telefonica", 1, "240.00")
    r.aggiungi(f1)

    f2 = Fattura("2026/002", date(2026, 2, 3), "Studio Verdi")
    f2.aggiungi_riga("Canone gestionale", 12, "85.00")
    f2.aggiungi_riga("Corso base per lo studio", 1, "400.00", "ridotta")
    r.aggiungi(f2)

    f3 = Fattura("2026/003", date(2026, 2, 28), "Studio Bianchi")
    f3.aggiungi_riga("Modulo dichiarativi", 1, "1200.00")
    r.aggiungi(f3)

    return r


if __name__ == "__main__":
    reg = registro_di_esempio()
    print(riepilogo_fattura(reg.trova("2026/001")))
    print()
    print(riepilogo_registro(reg))
