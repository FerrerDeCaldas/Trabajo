
#Ejercicio 1
def ejercicio_1():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    print("Nombre:", nombre)
    print("Edad:", edad)









#ejercicio 2
import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area
radio_circulo = 5
area_circulo = calcular_area_circulo(radio_circulo)
print("El área del círculo es:", area_circulo)






#ejerciocio 3
import random

def ejercicio_3():
    lista_numeros = [random.randint(1, 100) for _ in range(10)]
    print("Lista de números aleatorios:", lista_numeros)






#ejercicio 4
def es_par(numero):
    return numero % 2 == 0

numero_dado = 7
if es_par(numero_dado):
    print(numero_dado, "es par.")
else:
    print(numero_dado, "es impar.")






#ejercicio 5
def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5 / 9
    return grados_celsius


grados_fahrenheit = 68
grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(grados_fahrenheit, "grados Fahrenheit equivalen a", grados_celsius, "grados Celsius.")






#ejercicio 6
def suma_lista(lista):
    suma = sum(lista)
    return suma
lista_numeros = [1, 2, 3, 4, 5]
suma_total = suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)







#ejercicio 7
def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo
lista_numeros = [10, 5, 23, 8, 2]
maximo, minimo = encontrar_maximo_minimo(lista_numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)






#ejercio 8
def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida
lista_numeros = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista_numeros)
print("Lista invertida:", lista_invertida)







#ejercicio 9
def generar_matriz(filas, columnas):
    matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
filas = 3
columnas = 4
matriz_numeros = generar_matriz(filas, columnas)
print("Matriz generada:")
imprimir_matriz(matriz_numeros)








#ejercicio 10
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
numero_dado = 5
resultado_factorial = factorial(numero_dado)
print("El factorial de", numero_dado, "es:", resultado_factorial)






#ejercicio 11
def numeros_pares():
    lista_pares = [num for num in range(2, 101) if num % 2 == 0]
    return lista_pares
lista_pares_generada = numeros_pares()
print("Lista de números pares entre 1 y 100:", lista_pares_generada)





#ejercicio 12
def imprimir_numeros_del_1_al_10():
    for numero in range(1, 11):
        print(numero)





#ejercicio 13
def operaciones_aritmeticas(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones_aritmeticas(numero1, numero2)
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)





#ejercicio 14
def media_aritmetica(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media
lista_numeros = [10, 20, 30, 40, 50]
media = media_aritmetica(lista_numeros)
print("La media aritmética de la lista es:", media)






#ejercicio 5
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]
cadena_usuario = input("Ingrese una cadena de texto: ")
if es_palindromo(cadena_usuario):
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")