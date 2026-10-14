"""
Autore: Lorenzo Airoldi
Data: 07/10/2026
Titolo: Terzo esercizio - Classe Calcolo

Input: un intero n per il fattoriale e per la somma, un intero per la tabellina.
Output: fattoriale di n, somma 1 + 2 + ... + n, tabellina di n
        e tutte le tabelline da 1 a 9.
"""

# Funzioni
class Calcolo:
    """
    Classe Calcolo con costruttore di default (senza parametri).
    Permette di eseguire vari calcoli su numeri interi.
    """

    def __init__(self):
        """
        Costruttore di default della classe Calcolo.
        Non accetta parametri formali e non restituisce valori.
        """
        pass

    def Factorial(self, n: int) -> int:
        """
        Calcola il fattoriale di un intero.
        Parametri formali: n (int), numero intero non negativo.
        Valore di ritorno: int, fattoriale di n (n!).
        """
        if n < 0:
            raise ValueError("Il fattoriale e' definito solo per interi non negativi.")
        risultato = 1  # Fattoriale in costruzione
        for i in range(2, n + 1):
            risultato *= i
        return risultato

    def Sum(self, n: int) -> int:
        """
        Calcola la somma dei primi n interi: 1 + 2 + 3 + ... + n.
        Parametri formali: n (int), numero intero non negativo.
        Valore di ritorno: int, somma dei primi n interi.
        """
        if n < 0:
            raise ValueError("n non puo' essere negativo.")
        totale = 0  # Somma in costruzione
        for i in range(1, n + 1):
            totale += i
        return totale

    def tableMult(self, n: int) -> None:
        """
        Crea e visualizza la tabellina di un dato intero.
        Parametri formali: n (int), numero intero di cui stampare la tabellina.
        Valore di ritorno: None, la tabellina viene stampata a video.
        """
        if n < 0:
            raise ValueError("n non puo' essere negativo.")
        print(f"Tabellina di {n}:")
        for i in range(1, 10):
            print(f"{n} x {i} = {n * i}")

    def allTablesMult(self) -> None:
        """
        Visualizza tutte le tabelline dei numeri interi da 1 a 9.
        Parametri formali: nessuno.
        Valore di ritorno: None, le tabelline vengono stampate a video.
        """
        for n in range(1, 10):
            self.tableMult(n)
            print()


# Programma principale: istanzia la classe Calcolo ed esegue
# fattoriale, somma e tabelline.
# Sezione di input dati
n_fattoriale = int(input("Numero intero non negativo per il fattoriale: "))
n_somma = int(input("Numero intero non negativo per la somma: "))
n_tabellina = int(input("Numero intero non negativo per la tabellina: "))

# Inizializzazioni variabili
calcolo = Calcolo()  # Oggetto della classe Calcolo
risultato_fattoriale = 0  # Fattoriale di n_fattoriale
risultato_somma = 0  # Somma 1 + 2 + ... + n_somma

# Elaborazione
risultato_fattoriale = calcolo.Factorial(n_fattoriale)
risultato_somma = calcolo.Sum(n_somma)

# Sezione di output
print(f"Fattoriale di {n_fattoriale}: {risultato_fattoriale}")
print(f"Somma dei primi {n_somma} interi: {risultato_somma}")
print()
calcolo.tableMult(n_tabellina)
print()
calcolo.allTablesMult()
