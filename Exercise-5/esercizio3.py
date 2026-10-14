"""Terzo Esercizio: Massimo e minimo in un dizionario"""


def massimo_minimo_dizionario(d):
    """Restituisce il valore massimo e minimo in un dizionario."""
    if not d:
        return None, None
    valori = d.values()
    return max(valori), min(valori)


# Script di test
dizionario_test = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
max_val, min_val = massimo_minimo_dizionario(dizionario_test)
print(f"Terzo Esercizio - Massimo: {max_val}, Minimo: {min_val}")
print()