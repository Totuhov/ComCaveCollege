from Models.tier import Tier
from Models.schaf import Schaf
from Models.lamm import Lamm
from Models.schwein import Schwein
from Models.ferkel import Ferkel
from Models.kuh import Kuh
from Models.kalb import Kalb

schaf = Schaf("Shon", "Weiß", 15)

print(schaf.gewicht)

lamm = Lamm("Shon", "Weiß", 15, "Grün")

print(lamm.augenfarbe)

tier = Tier("Shon", "Weiß", 15)

print(tier.name)

dora = Kuh()

print(f"Dora hat gewicht von {dora.gewicht} kg")