## Cloud Specialist [ D68444-15-2025-23 ]

Unità Formativa : Programmazione Python

Docente: Massimo PAPA

Titolo argomento: Esercizi sui dizionari


## Esercizi sui dizionari


## Indicazioni sulla consegna

Implementare gli algoritmi risolutivi dei seguenti esercizi codificandoli in linguaggio python. Partire analizzando il problema seguendo la seguente traccia:

- Quali sono gli input del problema?

- Quali sono gli output?

- Suddividi il problema in problemi più semplici e se lo ritieni opportuno descrivi la soluzione di ogni sottoproblema con un flow-chart

- Andrai a rappresentare ogni algoritmo che risolve un sottoproblema come una funzione

- La funzione restituisce un valore? Se si di che tipo?

- Ogni funzione accetta una lista di parametri formali? Se si di che tipo?

- Esegui la codifica partendo dal programma principale, al suo interno vai a richiamare le funzioni che poi andrai successivamente a definire.

- Continua la codifica dichiarando e definendo tutte le funzioni prima del programma principale che richiama tutte le altre. In testa alle funzioni scrivi un commento che descrive la funzione stessa , cosa restituisce e quali sono i parametri formali.

- Scrivi la sezione dell’inizializzazione variabili scrivendo in un commento il significa della variabile stessa

- Verifica la codifica utilizzando input di test, cercando di provare anche i casi limite.

Attenzione: non utilizzare strutture complesse oltre ai dizionari e alle strutture viste sino a ora


## Struttura del codice sorgente

Relativamente alle indicazioni di scrittura del codice, utilizza il seguente schema generale:

```
‘’’
Autore: Nome Cognome
Data: gg/mm/aaaa
Titolo: Testo esercizio
‘’’
##
## Funzioni:
##
def fun(param1: int, param2: float) -> int:
‘’’
Funzione: fun
Template per costruire le funzioni
Parametri formali:
int Param1 -> descrizione Param1
float Param2 -> descrizione Param2
Valore di ritorno:
int -> descrizione valore di ritorno
‘’’
retValue = 5 # Valore di ritorno della funzione
return retValue
‘’’
Programma principale
Descrizione sintetica funzionalità
del programma principale.
‘’’
# Sezione di input Dati
# Inizializzazioni variabili
```

\# Elaborazione


```
\# Eventuali sotto processi di Elaborazione
# Sezione di output
```


## Esercizi sui Dizionari

## Primo Esercizio

Progettare una funzione che accetti un numero indefinito di dizionari e restituisca un dizionario che è la concatenazione di tutti i dizionari indicati come parametro formale alla funzione. Scrivete uno script che utilizzi tale funzione.

```
Esempio:
diz1 = {'v1':1,'v2':2,'v3':3}
diz2 = {'v4':4,'v5':5,'v6':6}
diz3 = {'v7':7,'v8':8}
Dizionario restituito: {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4,
'v5': 5, 'v6': 6, 'v7': 7, 'v8': 8}
```

## Secondo Esercizio

Scrivete uno script Python per generare e stampare un dizionario che contenga un numero (compreso tra 1 e n) nella forma (x, x*x).

```
Esempio:
n = 5
Dizionario: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Terzo Esercizio

Scrivete un programma Python per ottenere il valore massimo e minimo in un dizionario.

## Quarto Esercizio

Scrivete un programma Python per rimuovere i duplicati dal dizionario.

## Quinto Esercizio

Scrivete un programma Python per creare un dizionario da una stringa. Le lettere della stringa rappresentano le chiavi, i valori rappresentano le occorrenze della chiave nella stringa

```
Esempio
stringa = “ciao mamma”
Dizionario: {'c': 1, 'i': 1, 'a': 3, ‘o’: 1, ‘ ‘:1,'m': 3}
```
