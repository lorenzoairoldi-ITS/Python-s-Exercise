"""
Autore: Lorenzo Airoldi
Data: 07/10/2026
Titolo: Secondo esercizio - Classe Rettangolo

Input: base e altezza di due rettangoli.
Output: area e perimetro di ciascun rettangolo e l'esito del confronto
        contenimento tra il primo e il secondo rettangolo.
"""

# Funzioni
class Rettangolo:
    """
    Classe Rettangolo.
    Attributi: base (float), altezza (float).
    """

    def __init__(self, base: float, altezza: float):
        """
        Costruttore della classe Rettangolo.
        Parametri formali: base (float), altezza (float).
        """
        self.base = base
        self.altezza = altezza

    # Getter e setter per l'attributo base
    def get_base(self) -> float:
        """Restituisce la base del rettangolo."""
        return self.base

    def set_base(self, base: float) -> None:
        """Imposta la base del rettangolo."""
        if base <= 0:
            raise ValueError("La base deve essere un valore positivo.")
        self.base = base

    # Getter e setter per l'attributo altezza
    def get_altezza(self) -> float:
        """Restituisce l'altezza del rettangolo."""
        return self.altezza

    def set_altezza(self, altezza: float) -> None:
        """Imposta l'altezza del rettangolo."""
        if altezza <= 0:
            raise ValueError("L'altezza deve essere un valore positivo.")
        self.altezza = altezza

    def area(self) -> float:
        """
        Calcola l'area del rettangolo.
        Valore di ritorno: float, area (base * altezza).
        """
        return self.base * self.altezza

    def perimetro(self) -> float:
        """
        Calcola il perimetro del rettangolo.
        Valore di ritorno: float, perimetro (2 * (base + altezza)).
        """
        return 2 * (self.base + self.altezza)

    def contiene(self, altro: "Rettangolo") -> bool:
        """
        Verifica se il rettangolo chiamante contiene il rettangolo parametro.
        Parametri formali: altro (Rettangolo), rettangolo da confrontare.
        Valore di ritorno: bool, True se contiene, False altrimenti.
        """
        # Secondo la traccia: la sua altezza e la sua base sono maggiori
        # rispettivamente della base e dell'altezza del secondo rettangolo.
        return self.altezza > altro.base and self.base > altro.altezza

    def __str__(self) -> str:
        """
        Override del metodo __str__.
        Valore di ritorno: stringa con base e altezza del rettangolo.
        """
        return f"Base: {self.base}, Altezza: {self.altezza}"


# Programma principale: calcola area e perimetro di due rettangoli
# e verifica se il primo contiene il secondo.
# Sezione di input dati
base1 = float(input("Base del primo rettangolo: "))
altezza1 = float(input("Altezza del primo rettangolo: "))
base2 = float(input("Base del secondo rettangolo: "))
altezza2 = float(input("Altezza del secondo rettangolo: "))

# Inizializzazioni variabili
rettangolo1 = Rettangolo(base1, altezza1)  # Primo oggetto Rettangolo
rettangolo2 = Rettangolo(base2, altezza2)  # Secondo oggetto Rettangolo

# Elaborazione
area1 = rettangolo1.area()  # Area del primo rettangolo
area2 = rettangolo2.area()  # Area del secondo rettangolo
perimetro1 = rettangolo1.perimetro()  # Perimetro del primo rettangolo
perimetro2 = rettangolo2.perimetro()  # Perimetro del secondo rettangolo
contenuto = rettangolo1.contiene(rettangolo2)  # Esito del confronto

# Sezione di output
print(rettangolo1)
print(f"Area: {area1}, Perimetro: {perimetro1}")
print(rettangolo2)
print(f"Area: {area2}, Perimetro: {perimetro2}")
if contenuto:
    print("Il primo rettangolo contiene il secondo.")
else:
    print("Il primo rettangolo NON contiene il secondo.")
