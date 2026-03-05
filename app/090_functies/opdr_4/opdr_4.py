# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    # hier komt jouw code
    # Het woordje pass mag je weghalen
    result = []
    for persoon in lijst_met_namen:
        volledige_naam = persoon["voornaam"]
        if persoon["tussenvoegsel"]:
            volledige_naam += " " + persoon["tussenvoegsel"]
        volledige_naam += " " + persoon["achternaam"]
        result.append(volledige_naam)
    return result
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
for naam in volledige_naam(namen):
    print(naam)