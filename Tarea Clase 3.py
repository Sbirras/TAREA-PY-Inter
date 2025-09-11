#1- Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#   captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""

try:
    A = int(input("Ingrese el primer número: "))
    B = int(input("Ingrese el segundo número: "))
    resultado = A / B
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

"""
#2- Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#   de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
try:
    A = 5
    B = "10"
    resultado = A + B
    print("Resultado:", resultado)
except TypeError:
    print("Error: No se puede sumar un número con una cadena.")

"""

#3- Escribe un programa que intente acceder a una clave que no existe en un
#   diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
"""
datos_personales = {
    "nombre": "Gabo",
    "edad": 35,
    "ciudad": "Caseros"
}

try:
    profesion = datos_personales["profesion"]
    print("La profesión es:", profesion)
except KeyError as error:
    print(f"Error: La clave '{error.args[0]}' no existe en el diccionario.")



"""

#4-  Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#   FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#   embargo, también intenta crear el archivo si no existe.
"""

try:
    archivo = open("NoExiste.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado. Creando uno nuevo...")
    archivo = open("NoExiste.txt", "w")
    archivo.write("Archivo creado automáticamente.")
    archivo.close()
"""


#5- Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#   captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#   captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

"""

try:
    A = int(input("Ingrese el primer número: "))
    B = int(input("Ingrese el segundo número: "))
    resultado = A / B
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada inválida. Debe ingresar números.")
"""
