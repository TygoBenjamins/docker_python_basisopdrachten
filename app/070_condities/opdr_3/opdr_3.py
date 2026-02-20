# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...



input_leeftijd = int(input("Voer de leeftijd in: "))

if leeftijd["baby"][0] <= input_leeftijd <= leeftijd["baby"][1]:
    korting = normale_toegangsprijs * (kortings_percentages["baby"] / 100)
    print("De toegangsprijs is gratis voor baby's.")

elif leeftijd["kinderen"][0] <= input_leeftijd <= leeftijd["kinderen"][1]:
    print("Kinderen krijgen 50% korting.")
    korting = normale_toegangsprijs * (kortings_percentages["kinderen"] / 100)

elif leeftijd["volwassenen"][0] <= input_leeftijd <= leeftijd["volwassenen"][1]:
    print("Volwassenen betalen de normale toegangsprijs.")
    korting = normale_toegangsprijs * (kortings_percentages["volwassenen"] / 100)

elif leeftijd["ouderen"][0] <= input_leeftijd <= leeftijd["ouderen"][1]:
    print("Ouderen krijgen 30% korting.")
    korting = normale_toegangsprijs * (kortings_percentages["ouderen"] / 100)

else:
    print("Ongeldige leeftijd")
    korting = 0
toegangsprijs = normale_toegangsprijs - korting

print(f"De toegangsprijs is: {toegangsprijs:.2f} euro")
