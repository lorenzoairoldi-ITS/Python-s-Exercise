"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Liste - Cercare almeno un elemento comune

Input: due liste di numeri interi separati da spazi, anche vuote.
Output: OK se hanno almeno un elemento comune, altrimenti KO.
"""

# Funzioni
def hanno_elemento_comune(lista1: list, lista2: list) -> bool:
    """
    Cerca un elemento della prima lista anche nella seconda.
    Parametri formali: lista1 e lista2 (list), liste da confrontare.
    Valore di ritorno: bool, True se esiste almeno un elemento comune.
    """
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False


# Programma principale: legge due liste e verifica se hanno elementi comuni.
# Sezione di input dati
testo1 = input("Prima lista: inserisci interi separati da spazi: ")
testo2 = input("Seconda lista: inserisci interi separati da spazi: ")

# Inizializzazioni variabili
lista1 = []  # Numeri della prima lista
lista2 = []  # Numeri della seconda lista
comune = False  # Presenza di almeno un elemento comune

# Elaborazione
for valore in testo1.split():
    lista1.append(int(valore))
for valore in testo2.split():
    lista2.append(int(valore))
comune = hanno_elemento_comune(lista1, lista2)

# Sezione di output
if comune:
    print("OK")
else:
    print("KO")
