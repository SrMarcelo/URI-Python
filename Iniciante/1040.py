def calcula_media(notas: list):
    pesos = [2, 3, 4, 1]
    notaTotal = 0
    for i in range(4):
        notaTotal += notas[i] * pesos[i]

    return notaTotal/10.0


def avalia_exame(media: float):
    notaExame = float(input())
    print("Nota do exame: {0:.1f}".format(notaExame))
    novaMedia = (media + notaExame) / 2
    avalia_media(novaMedia)
    return novaMedia


def avalia_media(media: float):
    if media < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")


if __name__ == "__main__":
    notas = [float(nota) for nota in input().split()]
    media = calcula_media(notas)
    print("Media: {0:.1f}".format(media))
    if 5 <= media <= 6.9:
        print("Aluno em exame.")
        media = avalia_exame(media)
        print("Media final: {0:.1f}".format(media))
    else:
        avalia_media(media)
