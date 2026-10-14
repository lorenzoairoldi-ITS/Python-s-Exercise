"""
Autore: Lorenzo Airoldi
Data: 07/10/2026
Titolo: Primo esercizio - Classe Insegnante

Input: nome, eta' e stipendio di due insegnanti.
Output: gli attributi nome ed eta' di ciascun insegnante (tramite __str__)
        e lo stipendio privato letto tramite il metodo getter.
"""

# Funzioni
class Insegnante:
    """
    Classe Insegnante.
    Attributi: nome (str, pubblico), eta (int, pubblico), stipendio (float, privato).
    """

    def __init__(self, nome: str, eta: int, stipendio: float):
        """
        Costruttore della classe Insegnante.
        Parametri formali: nome (str), eta (int), stipendio (float, diventa privato).
        """
        self.nome = nome
        self.eta = eta
        self.__stipendio = stipendio  # Attributo privato

    # Getter e setter per l'attributo pubblico nome
    def get_nome(self) -> str:
        """Restituisce il nome dell'insegnante."""
        return self.nome

    def set_nome(self, nome: str) -> None:
        """Imposta il nome dell'insegnante."""
        self.nome = nome

    # Getter e setter per l'attributo pubblico eta
    def get_eta(self) -> int:
        """Restituisce l'eta' dell'insegnante."""
        return self.eta

    def set_eta(self, eta: int) -> None:
        """Imposta l'eta' dell'insegnante."""
        if eta < 0:
            raise ValueError("L'eta' non puo' essere negativa.")
        self.eta = eta

    # Getter e setter per l'attributo privato stipendio
    def get_stipendio(self) -> float:
        """Restituisce lo stipendio privato dell'insegnante."""
        return self.__stipendio

    def set_stipendio(self, stipendio: float) -> None:
        """Imposta lo stipendio privato dell'insegnante."""
        if stipendio < 0:
            raise ValueError("Lo stipendio non puo' essere negativo.")
        self.__stipendio = stipendio

    def __str__(self) -> str:
        """
        Override del metodo __str__.
        Valore di ritorno: stringa con gli attributi nome ed eta'.
        """
        return f"Nome: {self.nome}, Eta': {self.eta}"


# Programma principale: istanzia due oggetti Insegnante e ne stampa i dati.
# Sezione di input dati
nome1 = input("Nome del primo insegnante: ")
eta1 = int(input("Eta' del primo insegnante: "))
stipendio1 = float(input("Stipendio del primo insegnante: "))

nome2 = input("Nome del secondo insegnante: ")
eta2 = int(input("Eta' del secondo insegnante: "))
stipendio2 = float(input("Stipendio del secondo insegnante: "))

# Inizializzazioni variabili
insegnante1 = Insegnante(nome1, eta1, stipendio1)  # Primo oggetto Insegnante
insegnante2 = Insegnante(nome2, eta2, stipendio2)  # Secondo oggetto Insegnante

# Elaborazione
insegnante1.set_stipendio(insegnante1.get_stipendio() + 100)  # Aumento di prova

# Sezione di output
print(insegnante1)
print(insegnante2)
print(f"Stipendio di {insegnante1.get_nome()}: {insegnante1.get_stipendio()}")
print(f"Stipendio di {insegnante2.get_nome()}: {insegnante2.get_stipendio()}")
