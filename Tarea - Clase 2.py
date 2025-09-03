"""#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos..
A = {1, 2, 3}
B = {3, 4, 5}

union = A | B
print("Elementos en A o B o ambos:", union)"""

"""#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B
A = {1, 2, 3}
B = {3, 4, 5}

interseccion = A & B
print("Elementos en A y B:", interseccion)"""

"""#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
A = {1, 2, 3}
B = {3, 4, 5}

print("Elementos en A o B, no en ambos:", A.symmetric_difference(B))"""


#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))



"""#Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto
A = {1, 2, 3, 4, 5}

cantidad = len(A)
print("Cantidad de elementos en A:", cantidad)"""
