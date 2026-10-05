"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Stringhe - Rimuovere l'n-esimo carattere

Input: una stringa non vuota e una posizione definite nel codice.
Vincoli: posizione da 1 alla lunghezza della stringa; nessun input da tastiera.
Output: la stringa senza il carattere nella posizione indicata.
"""


# Funzioni
def rimuovi_carattere(testo: str, posizione: int) -> str:
    """
    Rimuove il carattere nella posizione indicata, contando da 1.
    Parametri formali: testo (str non vuota), posizione (int valido).
    Valore di ritorno: str, testo modificato.
    La validita' della posizione viene controllata nel programma principale.
    """
    indice = posizione - 1  # Indice Python del carattere da eliminare
    return testo[:indice] + testo[indice + 1 :]


# Programma principale: rimuove un carattere da un testo di esempio.
# Dati di esempio: modifica questi valori per provare altri casi.
testo = "Python"
posizione = 2  # Posizione del carattere da rimuovere, contando da 1

# Inizializzazioni variabili
risultato = ""  # Testo dopo la rimozione

# Elaborazione e sezione di output
if testo == "":
    print("La stringa non deve essere vuota.")
elif posizione < 1 or posizione > len(testo):
    print("Posizione non valida.")
else:
    risultato = rimuovi_carattere(testo, posizione)
    print("Stringa modificata:", risultato)
