#List
#List ist in Python das Array bzw. Vector(C/C++), ArrayList(Java)
zahlen = [1,2,3,4,5]
print(zahlen)
print(zahlen[-2])
print(len(zahlen))
print("-----")

woerter = ["Hallo", "Welt", "Peter", "Buch", "Volvo"]
print(woerter)

# Zur list hinzufügen
woerter.append("Motorad") 
woerter.insert(3, "Boot")
woerter.extend(zahlen)
print(woerter)
print("-----")

# Aus list entfernen
woerter.remove("Welt") #Entfernt spezifisches Element
woerter.pop(5) # Entfernt das Element am gegeben Index / ohne Index das letzte Element
del woerter[5]
print(woerter)
print("-----")

#Liste sortieren
woerter = ["Hallo", "Welt", "peter", "buch", "Volvo"]
print(woerter)
woerter.sort() # Sortiert die Liste aufsteigend - Case Sensitive
print(woerter)
woerter = ["Hallo", "Welt", "peter", "buch", "Volvo"]
woerter.sort(key= str.lower) # Sortiert die Liste aufsteigend - Case Insensitive
print(woerter)
woerter = ["Hallo", "Welt", "peter", "buch", "Volvo"]
woerter.sort(reverse=True) # Sortiert die Liste absteigend
print(woerter)
woerter = ["Hallo", "Welt", "peter", "buch", "Volvo"]
woerter.reverse()
print(woerter)

# Liste kopieren
woerter = ["Hallo", "Welt", "peter", "buch", "Volvo"]
wortliste = woerter.copy()
wortsammlung = list(woerter)

# Multidimensionale List
print("-----")
matrix = [[1,2,3],[4,5,6]]
print(matrix)
print(matrix[0][1])