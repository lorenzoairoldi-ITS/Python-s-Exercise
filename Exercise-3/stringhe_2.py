"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Stringhe - Verificare se una stringa e' palindroma

Input: una stringa.
Output: PALINDROMA oppure NON PALINDROMA.
Il confronto distingue maiuscole, minuscole, spazi e punteggiatura.
La stringa vuota e quella di un solo carattere sono palindrome.
"""

# Funzioni
def verifica_palindroma(testo: str) -> bool:
    """
    Confronta il testo con la sua versione invertita.
    Parametri formali: testo (str), stringa da controllare.
    Valore di ritorno: bool, True se la stringa e' palindroma.
    """
    return testo == testo[::-1]


# Programma principale: legge e controlla una stringa.
# Sezione di input dati
testo = input("Inserisci una stringa: ")

# Inizializzazioni variabili
palindroma = False  # Esito del controllo

# Elaborazione
palindroma = verifica_palindroma(testo)

# Sezione di output
if palindroma:
    print("PALINDROMA")
else:
    print("NON PALINDROMA")
