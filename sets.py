# Union
# Une todos los elementos
myset1 = {3,4,5}
myset2 = {5,6,7}
myset4 = {8,9,10}
myset3 = myset1 | myset2 | myset4
print(myset3) # {3, 4, 5, 6, 7, 8, 9, 10}

# Interseccion
# Solo une los elementos que tienen en comun
myset1 = {5,3,4}
myset2 = {5,6,7}
myset4 = {5,9,10}
myset3 = myset1 & myset2 & myset4
print(myset3) # {5}

# Diferencia
# Tomar dos sets de uno quitar todos los elementos que tiene el otro
myset1 = {3,4,5}
myset2 = {5,6,7}
myset3 = myset1 - myset2
print(myset3) # {3, 4}
myset4 = myset2 - myset1
print(myset4) # {6, 7}

# Diferencia Simetrica
# Se queda con todos los elementos de ambos set, pero lo que no se comparten
myset1 = {3,4,5}
myset2 = {5,6,7}
myset3 = myset1 ^ myset2
print(myset3) # {3, 4, 6, 7}

