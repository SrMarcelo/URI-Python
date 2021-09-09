def ordena_numeros(numeros: list):
    for i in range(1, len(numeros)):
        posicaoAnterior = i - 1
        while posicaoAnterior >= 0:
            posicaoAtual = posicaoAnterior + 1
            if numeros[posicaoAtual] < numeros[posicaoAnterior]:
                numeros[posicaoAnterior], numeros[posicaoAtual] = numeros[posicaoAtual], numeros[posicaoAnterior]
            else:
                break
            posicaoAnterior -= 1


if __name__ == "__main__":
    entradas = [int(entrada) for entrada in input().split()]
    entradasOriginal = tuple(entradas)
    ordena_numeros(entradas)
    for num in entradas:
        print(num)
    print()
    for num in entradasOriginal:
        print(num)

