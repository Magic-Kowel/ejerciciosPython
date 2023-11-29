frase = (input("Introduce una frase: "))
letra = (input("Introduce una letra: "))


contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print("La letra aparecio la cantidad de "+ str(contador))