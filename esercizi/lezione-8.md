# Lezione 8 - Git e ChatGPT insieme

Gli esercizi si fanno sul proprio ramo. Nessuno di questi testi va
incollato in una chat personale: si usa l'utenza aziendale.

## 1. Il messaggio di commit

Fare una modifica che tocchi due file. Poi, senza scriverlo a mano:

```
git diff --staged
```

Copiare la differenza e chiedere:

> Questa è la modifica che sto per salvare. Scrivimi il messaggio di commit
> seguendo queste regole: prima riga sotto i settanta caratteri, in italiano,
> al presente, che dice cosa fa il commit. Se serve un perché, mettilo nel
> corpo dopo una riga vuota.

Verifica: il messaggio proposto rispetta le regole di CONTRIBUTING.md.
Se non le rispetta, la richiesta era scritta male: correggerla.

## 2. Farsi spiegare una storia

```
git log --oneline -15
```

> Questa è la storia recente del progetto. Riassumimi cosa è successo
> in cinque righe, per qualcuno che rientra da tre settimane di assenza.

Verifica: il riassunto regge il confronto con la storia vera.

## 3. La descrizione della proposta

```
git diff main...HEAD
```

> Da questa differenza scrivimi la descrizione della proposta di modifica.
> Deve dire cosa cambia, perché, e come si verifica che funzioni.

Verifica: la parte "come si verifica" contiene comandi eseguibili, non frasi generiche.

## 4. La revisione assistita

Prendere la differenza del ramo `feature/sconto-riga`.

> Fammi la revisione di questa modifica. Elencami i problemi in ordine
> di gravità e per ognuno dimmi cosa succede in pratica se resta così.

Confrontare quello che segnala con quello che avevate trovato voi
nella lezione 7.

Verifica: si sa dire dove lo strumento ha visto qualcosa che era sfuggito,
e dove invece ha segnalato un falso problema.

## Cosa non si incolla mai

Credenziali, stringhe di connessione, chiavi. Dati di clienti degli studi.
Interi file di configurazione di produzione. Nel dubbio non si incolla.
