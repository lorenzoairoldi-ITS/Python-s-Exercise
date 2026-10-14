"""Quinto Esercizio: Dizionario da stringa - conteggio lettere"""


def dizionario_da_stringa(stringa):
    """Crea un dizionario da una stringa: lettere=chiavi, occorrenze=valori."""
    risultato = {}
    for char in stringa:
        if char in risultato:
            risultato[char] += 1
        else:
            risultato[char] = 1
    return risultato


# Script di test
stringa = "ciao mamma"
dizionario_stringa = dizionario_da_stringa(stringa)
print(f"Quinto Esercizio - Dizionario da stringa: {dizionario_stringa}")