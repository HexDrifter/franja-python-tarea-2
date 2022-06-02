# Ejercicio 2: Escribir una función que calcule el área de un
# círculo y otra que calcule el volumen de un cilindro usando
# la primera función.
import math as mt

def calcularArea(radio):
    return float(mt.pi * (radio*radio))

def calcularVolumen(altura, radio):
    return calcularArea(radio)*altura

radio = int(input("Ingrese el rádio del círculo: "))

areaCirculo = calcularArea(radio)

print("El área del círculo es: ", round(areaCirculo,3))

altura = int(input("Ahora utilizando el círculo anterior, vamos a calcular un cilíndro, Ingrese la altura del dicho cilíndro: "))

volumen= calcularVolumen(altura, radio)

print("El volumen del cilíndro de radio ", radio, " es: ", round(volumen,3))
