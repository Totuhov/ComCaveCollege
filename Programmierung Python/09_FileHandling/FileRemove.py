# Dateien entfernen
import os

os.remove("09_FileHandling\demo2.txt") # Datei löschen

os.mkdir("09_FileHandling\\test") # Ordner erstellen
datei = open("09_FileHandling\\test\demo2.txt", "x")
os.rmdir("09_FileHandling\\test") # Ordner löschen - nur leere Ordner