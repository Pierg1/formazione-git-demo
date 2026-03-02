# Registro fatture

Progetto di prova usato nel corso **Git e ChatGPT** tenuto da Keus.
Non è software di produzione: serve solo ad avere qualcosa di vero su cui lavorare
durante le lezioni 5, 6, 7 e 8.

Tutti i nomi di studi, clienti e importi sono inventati.
Le persone che compaiono nella storia dei commit sono di fantasia.

## Cosa fa

Tiene un registro di fatture emesse e ne calcola imponibile, imposta e totale.

```
python3 esempio.py
```

```
Fattura 2026/001 del 15/01/2026
Cliente: Studio Bianchi
----------------------------------------------------------------
Canone gestionale                  12 x     85.00 =    1020.00
Assistenza telefonica               1 x    240.00 =     240.00
----------------------------------------------------------------
Imponibile                                             1260.00
Imposta                                                 277.20
Totale documento                                       1537.20
```

## Com'è fatto

| File | Cosa contiene |
|---|---|
| `registro/iva.py` | Le aliquote, l'arrotondamento e il calcolo dell'imposta |
| `registro/fatture.py` | `Riga`, `Fattura` e `Registro` |
| `registro/report.py` | I riepiloghi in formato testo |
| `esempio.py` | Un registro già popolato, da eseguire |
| `tests/` | I test, si lanciano con `pytest` |
| `esercizi/` | Le tracce degli esercizi delle lezioni |

## Come si parte

Serve Python 3.10 o superiore.

```
git clone https://github.com/Pierg1/formazione-git-demo.git
cd formazione-git-demo
pip install pytest
python3 -m pytest
```

I test devono passare tutti. Se non passano, il problema è nell'ambiente,
non nel progetto: segnalarlo prima di iniziare gli esercizi.

## I rami preparati

| Ramo | A cosa serve |
|---|---|
| `main` | Il ramo principale. Non ci si lavora sopra direttamente. |
| `feature/sconto-riga` | Una modifica già scritta, con la sua proposta aperta. Si usa nella lezione 7 per esercitarsi sulla revisione. |
| `esercizio/conflitto` | Tocca le stesse righe che `main` ha cambiato dopo. Serve a generare un conflitto vero da risolvere. |

## Durante il corso

Nessuno lavora direttamente su `main`. Ogni esercizio si fa su un ramo proprio,
con il proprio nome dentro: `esercizio/nome-cognome`.

Le convenzioni su rami e messaggi di commit sono in [CONTRIBUTING.md](CONTRIBUTING.md).
