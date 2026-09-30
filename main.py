from Brano import Brano
from CD import CD
from Video import Video

# Brani
b1 = Brano("Unravel", "TK", 240)
b2 = Brano("Again", "YUI", 215)
b3 = Brano("Gurenge", "LiSA", 228)
print(b1)
print(b1.short_song())
b1.set_titolo("Unravel (TV size)")
print(b1.short_song())

# CD
cd = CD("Anime Hits", "AA.VV.", [b1, b2])
cd.aggiungi_brano(b3)
print(cd)
cd.rimuovi_brano("Again")
print("Durata dopo rimozione:", cd.durata_totale())

# Classi extra
v = Video("Making of", "Studio X", 600)
for e in (b2, v, p):
    pl.aggiungi(e)
print(pl)
