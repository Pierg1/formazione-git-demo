# Lezione 6 - Git, cos'è

Esercizi da svolgere sulla propria copia del progetto.
Ogni esercizio si chiude quando il comando di verifica dà il risultato indicato.

## 1. La prima copia

```
git clone https://github.com/Pierg1/formazione-git-demo.git
cd formazione-git-demo
git status
```

Verifica: `git status` risponde che non ci sono modifiche in sospeso.

## 2. Leggere la storia

```
git log --oneline
git log --oneline --stat
git show HEAD
```

Domande a cui rispondere leggendo la storia, senza aprire i file:

- Quanti commit ci sono su `main`?
- Chi ha scritto il calcolo dell'IVA?
- Quale commit ha un messaggio scritto male, e perché è scritto male?
- Qual è l'ultimo commit che ha toccato `registro/report.py`?

## 3. Il primo commit

Aprire `esempio.py` e aggiungere una quarta fattura al registro di esempio.

```
git status
git diff
git add esempio.py
git commit -m "Aggiunge una quarta fattura al registro di esempio"
git log --oneline -1
```

Verifica: il proprio commit è in cima a `git log`.

## 4. Tornare indietro

Modificare `registro/report.py` cambiando la larghezza del riepilogo,
poi annullare la modifica **senza** averla salvata in un commit.

```
git diff
git restore registro/report.py
git status
```

Poi fare una modifica, salvarla in un commit, e annullare quel commit
lasciando le modifiche nel file:

```
git commit -am "Prova da annullare"
git reset --soft HEAD~1
git status
```

Verifica: il commit non c'è più in `git log`, ma la modifica è ancora lì.
