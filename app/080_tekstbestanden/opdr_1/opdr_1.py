# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = "wat vind jij van de huidige regering? "
vraag2 = "wat vind jij van de python cursus? "
vraag3 = "wat vind jij de mooiste stad van Nederland? "

vragen = [vraag1, vraag2, vraag3]

for vraag in vragen:
    antwoord = input(vraag)
    print(f"Je antwoord op de vraag '{vraag}' is: {antwoord}")
    with open("antwoord.txt", "at") as fo:
        fo.write(f"Vraag: {vraag}\n")
        fo.write(f"Antwoord: {antwoord}\n\n")

fo = open("antwoord.txt", "at")
