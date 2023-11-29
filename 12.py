altura = int(input("Introduce un número entero: "))
while altura <=1:
    altura = int(input("Introduce un número entero: "))
for i in range(1, altura + 1):
    print('*' * i)