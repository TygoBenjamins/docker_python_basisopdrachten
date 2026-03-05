# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

encrypted_tekst = "Deze zin wil ik gaan encrypten, dat lijkt me leuk!"
# Schrijf hier je code om de tekst te encrypten en op te slaan in een bestand
print(encrypted_tekst)
for char in encrypted_tekst:
    if char.isalpha():  # Controleer of het een letter is
        shift = 3  # Aantal posities om te verschuiven
        if char.islower():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        encrypted_tekst += encrypted_char

print(encrypted_tekst)