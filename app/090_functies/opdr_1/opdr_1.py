# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    with open(afile, "at") as file:
        file.write(atext + "\n")

my_file = "test.txt"
my_tekst = "Dit is een test"
write_to_file(my_file, my_tekst)

