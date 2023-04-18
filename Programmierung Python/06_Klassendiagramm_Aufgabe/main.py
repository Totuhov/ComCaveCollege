from veranstaltung import *
from mitarbeiter import *

l1 = location_class.Location("Halle", "Berlin")

m1 = catering_class.Catering("Klaus")
m2 = sicherheit_class.Sicherheit("Herbert")

v1 = veranstaltung_class.Veranstaltung("V1")
v1.setLocation(l1)
v1.setArt(veranstaltungsart_enum.Veranstaltungsart.MARKTPLATZ)
v1.addMitarbeiter(m1)
v1.addMitarbeiter(m2)

v2 = veranstaltung_class.Veranstaltung("V2")
v2.setLocation(l1)
v2.setArt(veranstaltungsart_enum.Veranstaltungsart.MARKTPLATZ)
v2.addMitarbeiter(m1)
v2.addMitarbeiter(m2)

t1 = tournee_class.Tournee("Tournee 1")
t1.addVeranstaltung(v1)
t1.addVeranstaltung(v2)
print(t1)

#name = input("Bitte Namen eingeben:")
#print(name)

#zahl = int(input("Bitte eine Zahl eingeben:"))
#print(zahl * 5)

#name, ort = input("Bitte Name und Ort eingeben").split(",")
#print(name)
#print(ort)


#zahlen = [int(zahl) for zahl in input("Bitte Zahlen eingeben").split(",")]
#print(zahlen)

neueLocation = location_class.Location(input("Bitte Name eingeben"),input("Bitte Ort eingeben"))
print(neueLocation)