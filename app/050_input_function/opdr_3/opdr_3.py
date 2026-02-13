# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
stad1 = input("Voer de naam van de eerste stad in: ")
stad2 = input("Voer de naam van de tweede stad in: ")
stad3 = input("Voer de naam van de derde stad in: ")
stad4 = input("Voer de naam van de vierde stad in: ")
stad5 = input("Voer de naam van de vijfde stad in: ")
print(f" {stad1}, {stad2}, {stad3}, {stad4} en {stad5}")
sort_by = input("Wil je de steden op z-a alfabetische volgorde sorteren? (ja/nee): ")
steden = [stad1, stad2, stad3, stad4, stad5]
if sort_by.lower() == "ja":
    steden.sort(reverse=True)
print(f"De steden in z-a alfabetische volgorde zijn: {', '.join(steden)}")

