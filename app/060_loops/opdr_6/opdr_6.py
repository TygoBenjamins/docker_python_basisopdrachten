# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = [['verdi', 'calzone', 'margharita', 'olivio', 'quattro stagioni']]

my_list[0].sort(reverse=False)
print(my_list)

my_list.extend([['yo-favorito']])
print(my_list)

my_list[0].remove('olivio')
print(my_list)

pizza = my_list[0][0:3]
print(pizza)

pizza1 = my_list[0][2:3]
print(pizza1)

pizza2 = my_list[0][1:5]
print(pizza2)