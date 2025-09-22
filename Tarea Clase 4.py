##Calcular el mayor de dos números ingresados por teclado usando un operador
##ternario
"""a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
mayor = a if a > b else b
print(f"El mayor es: {mayor}")"""

##Buscar una palabra en una lista ingresada por teclado usando args y un operador
##ternario
"""def buscar_numero(numero, *args):
    mensaje = "Número encontrado" if numero in args else "Número no encontrado"
    print(mensaje)

buscar_numero(42, 10, 23, 42, 8, 15)"""

#Determinar si un número es par o impar
"""numero = int(input("Ingrese un número: "))
print("Par" if numero % 2 == 0 else "Impar")"""

#Calcular el promedio de una lista de números usando args y un operador ternario
"""def promedio(*args):
    resultado = sum(args) / len(args) if len(args) > 0 else "No hay números"
    print(f"Promedio: {resultado}")

promedio(4, 8, 15, 16, 23, 42)"""

#Imprimir un mensaje de error si no se pasan suficientes argumentos
"""def verificar_argumentos(*args):
    print("Argumentos suficientes" if len(args) >= 3 else "Error: se requieren al menos 3 argumentos")

verificar_argumentos(1, 2)
"""

