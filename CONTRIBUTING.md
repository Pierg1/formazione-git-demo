# Convenzioni

Regole del progetto di prova. Sono volutamente poche: servono a far vedere
che una convenzione scritta vale più di una convenzione sottintesa.

## Rami

Il ramo principale è `main` ed è protetto: non ci si scrive sopra direttamente.

Ogni lavoro parte da `main` aggiornato e va su un ramo proprio:

```
git switch main
git pull
git switch -c esercizio/nome-cognome
```

Nomi dei rami, per tipo di lavoro:

| Prefisso | Quando |
|---|---|
| `feature/` | Una funzione nuova |
| `fix/` | La correzione di un difetto |
| `esercizio/` | Il lavoro di un partecipante durante il corso |

Un ramo vive pochi giorni. Più resta aperto, più diverge da `main` e più
sarà doloroso riportarlo indietro.

## Messaggi di commit

Prima riga: massimo settanta caratteri, in italiano, al presente, che dice
**cosa fa il commit**, non cosa ha fatto la persona.

```
Aggiunge il calcolo dell'IVA ridotta
Corregge l'arrotondamento sui totali di riga
Toglie il codice non più raggiungibile in report
```

Non così:

```
fix
modifiche varie
ho sistemato quella cosa di ieri
aggiornamento
```

Se serve spiegare **perché**, si lascia una riga vuota e si scrive sotto.
La prima riga risponde a "cosa", il corpo risponde a "perché".

```
Corregge l'arrotondamento sui totali di riga

Su quantità alte l'errore del centesimo si accumulava e il totale
documento non tornava con quello del gestionale dello studio.
```

## Un commit, una cosa

Un commit contiene una modifica sola. Se nel messaggio serve una "e"
per descriverlo, quasi sempre sono due commit.

## Prima di aprire una proposta di modifica

1. I test passano: `python3 -m pytest`
2. Il ramo è aggiornato con `main`
3. La descrizione dice cosa cambia e come si verifica

## Revisione

Chi rivede guarda tre cose, in quest'ordine: che risolva il problema,
che non ne apra altri, che si riesca a rileggere fra sei mesi.

I commenti si scrivono sul codice, non sulla persona. "Questa funzione
fa due cose" va bene, "non hai capito il requisito" no.
