# Dictionary
# Ein Dictionary ist eine geordnet Sammlung von Key:Value Paaren

auto = {"Marke" : "Ford", "Model": "Mustang", "Baujahr" : 1964}
print(auto)
print(auto["Marke"])

# Elemente hinzufügen
auto["Baujahr"] = "1999" # verändern des Wertes
auto["Farbe"] = "rot"
print(auto)
auto.update({"Baujahr": "1977"})
print(auto)

# Elemente löschen
auto.pop("Farbe")
print(auto)
auto.popitem() #entfernt das letzte hinzugefügte Element
print(auto)

# Mehrdim Dictionary
spiele = {
    "Doom": {
        "Genre" : "Shooter", "Release": "1994"
    }, 
    "Fifa":{
        "Genre":"Sport"
    }}
print(spiele)
print(spiele["Doom"])
print(spiele["Doom"]["Release"])

#spiele.update(["Doom"]{"Genre": "Simulation"})
#spiele.update({"Doom":{"Genre": "Simulation"}})
#spiele.update({"Doom"},{"Genre": "Simulation"})
spiele["Doom"]["Genre"] = "Simulation"
print(spiele)