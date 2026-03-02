# Lezione 7 - Git nel team

## 1. Il proprio ramo

```
git switch main
git pull
git switch -c esercizio/nome-cognome
```

Aggiungere l'aliquota `"agevolata"` al 5 per cento in `registro/iva.py`,
con il relativo test in `tests/test_iva.py`.

```
python3 -m pytest
git add -A
git commit -m "Aggiunge l'aliquota agevolata al 5 per cento"
git push -u origin esercizio/nome-cognome
```

Verifica: i test passano e il ramo si vede su GitHub.

## 2. La proposta di modifica

Aprire una pull request dal proprio ramo verso `main`.
La descrizione deve dire tre cose: cosa cambia, perché, come si verifica.

Verifica: la pull request è aperta e la descrizione risponde alle tre domande.

## 3. La revisione

Guardare il ramo `feature/sconto-riga` e la sua proposta già aperta.

```
git fetch origin
git switch feature/sconto-riga
git diff main...feature/sconto-riga
python3 -m pytest
```

Scrivere almeno due commenti di revisione. Almeno uno deve riguardare
qualcosa che non va: la modifica ha un difetto voluto.

Verifica: i commenti sono sul codice, non sulla persona, e almeno uno
segnala il difetto vero.

## 4. Il conflitto

```
git switch main
git pull
git switch esercizio/conflitto
git merge main
```

Git si ferma e segnala un conflitto su `registro/iva.py`.
Aprire il file, capire quale delle due versioni va tenuta e perché,
risolvere, poi:

```
python3 -m pytest
git add registro/iva.py
git commit
```

Verifica: i test passano e `git log --graph --oneline -12` mostra la fusione.
