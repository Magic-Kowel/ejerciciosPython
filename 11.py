numero = int(input("Introduce un número entero positivo"))
lista=[]
while numero <=1:
    numero = int(input("Introduce un número entero positivo"))

for item in range(1,numero):
    if(item % 2 != 0):
        lista.append(str(item))
    else:
        continue 
resultado = ', '.join(lista)

print(resultado)