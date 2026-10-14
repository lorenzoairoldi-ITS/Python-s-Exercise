"""Secondo Esercizio: Dizionario numeri e quadrati"""


def genera_dizionario_quadrati(n):
    """Genera un dizionario con numeri da 1 a n come chiavi e i loro quadrati come valori."""
    return {x: x*x for x in range(1, n+1)}


# Script di test
n = 5
dizionario = genera_dizionario_quadrati(n)
print(f"Secondo Esercizio - Dizionario: {dizionario}")
print()