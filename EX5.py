numeroTelefone = input("Infome um número de telefone: ")

numero_telefone_tratado =[]

for numero in numeroTelefone:
    if numero.isdigit():
        numero_telefone_tratado.append(numero)

if len(numero_telefone_tratado) == 7:
    numero_telefone_tratado.insert(0, 3)

print(numero_telefone_tratado)


