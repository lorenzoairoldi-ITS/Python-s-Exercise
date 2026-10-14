"""Quarto Esercizio: Rimuovi duplicati da un dizionario"""


def rimuovi_duplicati_dizionario(d):
    """Rimuove i duplicati dai valori di un dizionario, mantenendo la prima chiave per ogni valore."""
    valori_unici = {}
    for k, v in d.items():
        if v not in valori_unici:
            valori_unici[v] = k
    return valori_unici


# Script di test
dizionario_test2 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
dizionario_pulito = rimuovi_duplicati_dizionario(dizionario_test2)
print(f"Quarto Esercizio - Dizionario senza duplicati: {dizionario_pulito}")
print()