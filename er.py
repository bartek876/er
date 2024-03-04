class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model


    def opis(self):
        return f"Pojazd marki {self.marka}, model {self.model}."
   
class Łódka(Pojazd):
    def __init__(self, marka, model, rok_produkcji,długość,wysokość):
        super().__init__(marka, model)
        self.rok_produkcji = rok_produkcji
        self.długość = długość
        self.wysokość = wysokość

    def opis(self):
        bazowy_opis = super().opis()
        return f"{bazowy_opis} Rok produkcji: {self.rok_produkcji},długość{self.długość}metrów, wysokość{self.wysokość}metrów"
   
a = Łódka("Mitsubishi", "5xc", 1941,234)
print(a.opis())
class Samochód(Pojazd):
    def __init__(self, marka, model, rok_produkcji):
        super().__init__(marka, model)
        self.rok_produkcji = rok_produkcji


    def opis(self):
        bazowy_opis = super().opis()
        return f"{bazowy_opis} Rok produkcji: {self.rok_produkcji}."
   
a = Samochód("Toyota", "Corolla", 2020)
print(a.opis())