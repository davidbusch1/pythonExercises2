frase = input("Informe uma frase: ")

espacoBranco = frase.count(" ")

vogal_a = frase.count("a")
vogal_e = frase.count("e")
vogal_i = frase.count("i")
vogal_o = frase.count("o")
vogal_u = frase.count("u")

print(f"Há {espacoBranco} espacos em branco na frase")
print(f"A vogal a aparece {vogal_a} vezes")
print(f"A vogal e aparece {vogal_e} vezes")
print(f"A vogal i aparece {vogal_i} vezes")
print(f"A vogal o aparece {vogal_o} vezes")
print(f"A vogal u aparece {vogal_u} vezes")