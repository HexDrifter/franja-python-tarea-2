
# Ejercicio 3: Escribir un programa para una empresa que tiene
# salas de juegos para todas las edades y quiere calcular de forma
# automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y
# mostrar el precio de la entrada. Si el cliente es menor de 4 años
# puede entrar gratis, si tiene entre 4 y 18 años debe pagar $3.500
# y si es mayor de 18 años, $8.000.

edad = int(input("Ingrese su edad"))
precio = int(0)
if edad < 4 :
    precio = int(0)
elif edad < 18 :
    precio = int(3500)
else:
    precio = int(8000)

print("El costo de la entrada es $", precio)
if precio == 0 :
    print("Usted entra gratis")
else:
    print("Usted debe pagar")