#Elabore um programa que efetue a leitura de duas strings e 
#informe o seu conteúdo, seguido de seu compri- mento. 
#Indique também se as duas strings possuem o mesmo comprimento e se são iguais ou diferentes no conteúdo.




string1 = input("Informe uma string: ")
string2 = input("Informe outra string: ")

print(f"O conteúdo da primeira string é: {string1}")
print(f"O conteúdo da segunda string é: {string2}")
print(f"O comprimento da primeira string é {len(string1)}")
print(f"O comprimento da segunda string é {len(string2)}")

print("O conteudo das string é o mesmo") if string1 == string2 \
    else print("O conteudo das string é diferente")
print("O comprimento das string é o mesmo") if len(string1) == len(string2) \
    else print("O comprimento das string é diferente")
