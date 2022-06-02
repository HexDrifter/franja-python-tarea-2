# Ejercicio 1: Escribir un programa en el que se pregunte al usuario
# por una frase y una letra, y muestre por pantalla el número de veces
# que aparece la letra en la frase. 

frase=input("Escriba una frase, para terminar presione Enter: ")

letra=input("Ahora ingrese una letra para buscar en la frase: ")

conteo = int(0)
for i in frase:
    if letra == i:
        conteo+=1

print("la letra ", letra," aparece ",conteo," veces en la frase")