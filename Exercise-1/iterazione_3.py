"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Iterazione - Terzo esercizio: successione crescente

Input: una successione di numeri interi.
Vincoli: ogni numero deve essere maggiore del precedente.
         Un numero minore o uguale al precedente termina la lettura.
Output: quanti numeri formano la successione crescente,
        escludendo il numero che interrompe la crescita.
"""

# Sezione di input dati
precedente = int(input("Inserisci il primo numero: "))

# Inizializzazioni variabili
contatore = 1

# Elaborazione e lettura dei numeri successivi
numero = int(input("Inserisci il numero successivo: "))
while numero > precedente:
    contatore = contatore + 1
    precedente = numero
    numero = int(input("Inserisci il numero successivo: "))

# Sezione di output
print("Numeri della successione crescente:", contatore)
