# Set
# Sets sind ungeordnette, unveränderliche*  Sammlungen
# *Die Werte sind unveränderlich, aber ein Set kann weitere Elemente aufnehmen oder löschen
# Die Elemente in einem Set sind einzigartig - Duplikate werden nicht zugelassen

# Set erzeugen
woerter = {"Hallo", "Welt", "Python", "ist", "leicht"}
print(woerter)
zahlen = {6,7,8,9,1,1,2,2,3,3,4,4,5,0.5, 1.5675}
print(zahlen)

# Elemente einzeln aufrufen
for x in woerter:
    print(x)

# Elemente hinzufügen
zahlen.add(42)
print(zahlen)
woerter.add("Insel")
print(woerter)

# Elemente löschen
woerter.remove("Welt")
print(woerter)

print(woerter.pop()) # pop() entfernt ein zufälliges Element und gibt dieses auch zurück

# Set zusammenfügen
woerter.update(zahlen)
print(woerter)