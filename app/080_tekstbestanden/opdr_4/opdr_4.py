# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
vraag1 = "Wat is je voornaam?"
vraag2 = "Wat is je achternaam?"
vraag3 = "wat neem je mee aan drinken?"
vraag4 = "Wat neem je mee aan eten?"
antwoord1 = input(vraag1)
antwoord2 = input(vraag2)
antwoord3 = input(vraag3)
antwoord4 = input(vraag4)
afsluiting = "Bedankt voor het invullen van de enquete!"
print("afsluiting)")


# Opslaan in een tekstbestand
with open("enquete.txt", "w") as file:
    file.write(vraag1 + " " + antwoord1 + "\n")
    file.write(vraag2 + " " + antwoord2 + "\n")
    file.write(vraag3 + " " + antwoord3 + "\n")
    file.write(vraag4 + " " + antwoord4 + "\n")
    file.write(afsluiting + "\n")

