"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Iterazione - Secondo esercizio: media dei saldi negativi

Input: numero N di conti e i loro saldi.
Vincoli: N intero positivo; nella media si considerano solo saldi < 0.
Output: media dei saldi negativi, oppure un messaggio se non ce ne sono.
"""

# Sezione di input dati
n = int(input("Quanti conti vuoi inserire? "))

# Inizializzazioni variabili
somma = 0
contatore = 0
media = 0

# Elaborazione e lettura dei saldi
if n > 0:
    for i in range(n):
        saldo = float(input("Inserisci il saldo del conto: "))
        if saldo < 0:
            somma = somma + saldo
            contatore = contatore + 1
    if contatore > 0:
        media = somma / contatore

# Sezione di output
if n <= 0:
    print("Il numero di conti deve essere positivo.")
elif contatore == 0:
    print("Non ci sono saldi negativi.")
else:
    print("Media dei saldi negativi:", media)
