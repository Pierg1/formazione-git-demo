"""Riepiloghi leggibili a partire dal registro."""

LARGHEZZA = 64


def riga_separatrice(carattere="-"):
    return carattere * LARGHEZZA


def riepilogo_fattura(fattura):
    """Restituisce il riepilogo di una singola fattura come testo."""
    righe = [
        "Fattura %s del %s" % (fattura.numero, fattura.data.strftime("%d/%m/%Y")),
        "Cliente: %s" % fattura.cliente,
        riga_separatrice(),
    ]
    for r in fattura.righe:
        righe.append(
            "%-32s %4d x %9s = %10s"
            % (r.descrizione[:32], r.quantita, r.prezzo_unitario, r.imponibile)
        )
    righe.append(riga_separatrice())
    righe.append("%-48s %13s" % ("Imponibile", fattura.imponibile))
    righe.append("%-48s %13s" % ("Imposta", fattura.imposta))
    righe.append("%-48s %13s" % ("Totale documento", fattura.totale))
    return "\n".join(righe)


def riepilogo_registro(registro):
    """Restituisce il riepilogo dell'intero registro come testo."""
    righe = ["Registro fatture", riga_separatrice("=")]
    for f in registro:
        righe.append("%-12s %-28s %10s %10s" % (f.numero, f.cliente[:28], f.imponibile, f.totale))
    righe.append(riga_separatrice("="))
    righe.append("%-41s %10s %10s" % ("Totali", registro.totale_imponibile(), registro.totale_imposta()))
    righe.append("Documenti registrati: %d" % len(registro))
    return "\n".join(righe)
