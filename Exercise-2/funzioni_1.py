"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Primo esercizio - Confronto tra due quantita' di tempo

Input: ore, minuti e secondi di due durate.
Vincoli: valori interi non negativi; minuti e secondi compresi tra 0 e 59.
Output: quale durata e' maggiore oppure se le durate sono uguali.
"""

# Funzioni
def tempo_in_secondi(ore: int = 0, minuti: int = 0, secondi: int = 0) -> int:
    """
    Converte una durata in secondi.
    Parametri formali: ore, minuti e secondi (int), tutti predefiniti a zero.
    Valore di ritorno: int, numero totale di secondi.
    """
    totale = ore * 3600 + minuti * 60 + secondi  # Durata in secondi
    return totale


# Programma principale: legge e confronta due durate.
# Sezione di input dati
ore1 = int(input("Ore della prima durata: "))
minuti1 = int(input("Minuti della prima durata: "))
secondi1 = int(input("Secondi della prima durata: "))
ore2 = int(input("Ore della seconda durata: "))
minuti2 = int(input("Minuti della seconda durata: "))
secondi2 = int(input("Secondi della seconda durata: "))

# Inizializzazioni variabili
totale1 = 0  # Prima durata espressa in secondi
totale2 = 0  # Seconda durata espressa in secondi
messaggio = ""  # Esito del confronto o segnalazione di dati non validi

# Elaborazione
if (ore1 < 0 or ore2 < 0 or
        minuti1 < 0 or minuti1 > 59 or minuti2 < 0 or minuti2 > 59 or
        secondi1 < 0 or secondi1 > 59 or secondi2 < 0 or secondi2 > 59):
    messaggio = "Durate non valide: ore non negative, minuti e secondi tra 0 e 59."
else:
    totale1 = tempo_in_secondi(ore1, minuti1, secondi1)
    totale2 = tempo_in_secondi(ore2, minuti2, secondi2)
    if totale1 > totale2:
        messaggio = "La prima durata e' maggiore."
    elif totale2 > totale1:
        messaggio = "La seconda durata e' maggiore."
    else:
        messaggio = "Le due durate sono uguali."

# Sezione di output
print(messaggio)
