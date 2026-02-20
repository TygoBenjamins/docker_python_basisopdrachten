# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....


while True:
    try:
        gok = int(input(prompt))
    except ValueError :
        print("Ongeldige invoer. Voer een getal in tussen 1 en 100.")
        continue

    if gok < 1 or gok > 100:
        print("Ongeldige invoer. Voer een getal in tussen 1 en 100.")
        continue
    
    if gok < geheim_getal:
        print ("Te laag, probeer het opnieuw.")
    
    elif gok > geheim_getal:
        print("Te hoog, probeer het opnieuw.")
    else:
        print("Gefeliciteerd! Je hebt het geheime getal geraden.")
    if gok == geheim_getal:
        break