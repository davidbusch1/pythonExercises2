medias = []

alunos = 1

for aluno in range(0, 10):

    print(f"Informe as nota do {alunos}º aluno")

    media = 0
    nota = 1

    for notas in range(0, 4):
        media += float(input(f"Informe a {nota}º: "))
        nota += 1

    media /= 4
    medias.append(media)
    alunos += 1

for media in medias:
    if media >= 7:
        print(media)
