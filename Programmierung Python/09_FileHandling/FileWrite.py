# Datei schreiben / erstellen.

# Beim schreiben gibt es 2 Möglichkeiten.
# w - Schreiben
# a - Anhängen

datei = open("09_FileHandling\demo.txt", "w")
datei.write("Neuer Inhalt")
datei.close()

datei = open("09_FileHandling\demo.txt", "a")
datei.write("Neuer Inhalt")
datei.close()

datei = open("09_FileHandling\demo2.txt", "a")
woerter = ["Hallo\n", "Welt\n", "Python\n", "ist\n", "wunderbar\n"]
datei.writelines(woerter)
datei.close()

datei = open("09_FileHandling\demo2.txt", "x") # "x" Erstellt die Datei, gibt aber einen Fehler wenn diese schon vorhanden ist.