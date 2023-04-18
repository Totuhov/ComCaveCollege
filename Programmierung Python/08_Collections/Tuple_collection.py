# Tuples
# Eine geordnete, sequenzielle Sammlung - ist unveränderlich
# Nachdem ein Tuple erstellt worden ist, 
# können keine Elemente verändert oder gelöscht werden

# Tuple erzeugen
woerter = ("Hallo", "Welt", "Python", "ist", "leicht")
print(woerter)
print(woerter[2])
# !Wichtig - Tuple müssen immer mit "mehreren" Werten erzeugt werden!
zahlen = (1,)
print(zahlen)
print(zahlen[0])

# Tuple Update - Tuple können zusammengeführt werden
werte = (2,3)
zahlen += werte
print(zahlen)

# Workaround für Tuple-Veränderung - Tuple in List umwandeln, List verändern, List zu tupel wandeln
zahlenliste = list(zahlen)
zahlenliste.append(4)
zahlen = tuple(zahlenliste)
print(zahlen)

# Packen in ein Tuple - Einpacken als Tuple
buchstaben = tuple("Python")
print(buchstaben)

# Unpack - Tuple in mehrere Variablen wandeln
a,b,c,d,e,f = buchstaben
print(a)
print(e)
# - Es werden dieselbe anzahl variablen benötigt wie Elemente im Tuple
# Workaround: Asteriks * - Wandelt alle übrigen Elemente in eine liste
a,*b = buchstaben
print(a)
print(b)
print(buchstaben)

# Mehrdimensionales Tupel
mehrdim = (("Hallo", "Welt"), (42,50))
print(mehrdim)
print(mehrdim[0][1])