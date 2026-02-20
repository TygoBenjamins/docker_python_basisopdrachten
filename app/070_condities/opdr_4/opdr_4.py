# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [naam for naam, prijs in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...
if keuze in dict(toppings):
    prijs = dict(toppings)[keuze]
    print(f"De prijs van de gekozen topping is: {prijs:.2f} euro")
else:
    print("Sorry, deze topping is niet beschikbaar.")
    