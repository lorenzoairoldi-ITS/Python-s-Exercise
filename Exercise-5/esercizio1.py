"""Primo Esercizio: Concatenazione dizionari"""


def concatena_dizionari(*dizionari):
    """Accetta un numero indefinito di dizionari e restituisce un dizionario concatenato."""
    risultato = {}
    for d in dizionari:
        risultato.update(d)
    return risultato


# Script di test
diz1 = {'v1': 1, 'v2': 2, 'v3': 3}
diz2 = {'v4': 4, 'v5': 5, 'v6': 6}
diz3 = {'v7': 7, 'v8': 8}

dizionario_risultato = concatena_dizionari(diz1, diz2, diz3)
print(f"Primo Esercizio - Dizionario restituito: {dizionario_risultato}")
print()