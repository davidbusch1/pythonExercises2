caracter = []
vogais = ["a", "e", "i", "o", "u"]
contagemVogal = 0

for volta in range(1, 11):
    entrada = input(f"Caractere {volta}: ")
    caracter.append(entrada)

    if entrada in vogais:
        contagemVogal += 1

print("Consoantes: ", (len(caracter)) - contagemVogal)
