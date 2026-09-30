class Brano:
    def __init__(self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata  

    def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_autore(self):
        return self.autore

    def set_autore(self, autore):
        self.autore = autore

    def get_durata(self):
        return self.durata

    def set_durata(self, durata):
        self.durata = durata

    def short_song(self, max_len=15):
        """Versione breve: titolo abbreviato + durata in mm:ss."""
        titolo = self.titolo
        if len(titolo) > max_len:
            titolo = titolo[:max_len - 3] + "..."
        minuti, secondi = divmod(self.durata, 60)
        return f"{titolo} ({minuti}:{secondi:02d})"

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Durata: {self.durata}s"                 