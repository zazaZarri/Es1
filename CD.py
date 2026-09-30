from Brano import Brano


class CD:
    def __init__(self, titolo, autore, brani=None):
        self.titolo = titolo
        self.autore = autore
        self.brani = list(brani) if brani else []

    def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_autore(self):
        return self.autore

    def set_autore(self, autore):
        self.autore = autore

    def get_brani(self):
        return self.brani

    def aggiungi_brano(self, brano):
        self.brani.append(brano)

    def rimuovi_brano(self, titolo):
        self.brani = [b for b in self.brani if b.get_titolo() != titolo]

    def durata_totale(self):
        """Durata complessiva in secondi."""
        return sum(b.get_durata() for b in self.brani)

    def __str__(self):
        righe = [f"CD: {self.titolo}, Autore: {self.autore}, "
                 f"Durata totale: {self.durata_totale()}s"]
        for i, b in enumerate(self.brani, start=1):
            righe.append(f"  {i}. {b}")
        return "\n".join(righe)
