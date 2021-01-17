numeros =[]

for numero in range(0, 15):
    numeros.append(int(input("Informe um nuúmero inteiro: ")))

par = []
impar = []

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(numeros)
print(par)
print(impar)

