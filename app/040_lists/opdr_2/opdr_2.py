# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "Rijn": ["Nederland", "Duitsland", "Frankrijk"],
    "Maas": ["Nederland", "België", "Duitsland"],
    "nijl": ["Egypte", "Soedan", "Oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

print (rivieren[0])
print (rivier_info["Rijn"][1])
print (f"de {rivieren[0]} stroomt onder andere door {rivier_info['Rijn'][1]}")
print (rivier_info["Rijn"][0] + " en " + rivieren [0])
print (f"de {rivieren[1]} stroomt onder andere door {rivier_info['Maas'][0]}")

print (rivieren[-1])
print (rivieren[-1] + " " + rivier_info["nijl"][-1])
print (f"de {rivieren[-1]} stroomt onder andere door {rivier_info['nijl'][-1]}")