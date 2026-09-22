"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Terzo esercizio - Conversione da Fahrenheit a Celsius

Input: una temperatura reale espressa in gradi Fahrenheit.
Output: temperatura in gradi Celsius visualizzata con tre cifre decimali.
"""

# Funzioni
def convertiCF(fahrenheit: float) -> float:
    """
    Converte una temperatura da Fahrenheit a Celsius.
    Parametri formali: fahrenheit (float), temperatura da convertire.
    Valore di ritorno: float, temperatura in gradi Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9  # Temperatura convertita
    return celsius


# Programma principale: legge, converte e stampa la temperatura.
# Sezione di input dati
fahrenheit = float(input("Temperatura in gradi Fahrenheit: ").replace(",", "."))

# Inizializzazioni variabili
celsius = 0.0  # Temperatura risultante dalla conversione

# Elaborazione
celsius = convertiCF(fahrenheit)

# Sezione di output
print(f"Temperatura in gradi Celsius: {celsius:.3f}")
