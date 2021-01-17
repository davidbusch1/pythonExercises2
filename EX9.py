notas = []
media = 0

for nota in range(1, 6):
    notas.append(float(input(f"Informe a {nota}º nota: ")))
    media += notas[nota - 1]

media /= 5

print(notas)
print(round(media, 2))

if media >= 7:
    print("Aluno aprovado")
elif 4 <= media <= 7:
    print("Aluno em exame")
else:
    print("Aluno reprovado")
