# TextDatei lesen
# Dateiort relativ zum Arbeitsordner der Konsole beachten!
datei = open("09_FileHandling\demo.txt", "r")
print(datei.read()) # Gesamte Datei auslesen
datei.close()
datei = open("09_FileHandling\demo.txt", "r")
print(datei.read(5)) # Anzahl Zeichen auslesen
datei = open("09_FileHandling\demo.txt", "r")
print(datei.readline()) # Einzelne Zeile auslesen
print(datei.readline())