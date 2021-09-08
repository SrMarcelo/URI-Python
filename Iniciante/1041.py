def classifica_ponto(ponto: list):
    if ponto[0] > 0:
        if ponto[1] > 0:
            print("Q1")
        elif ponto[1] < 0:
            print("Q4")
        else:
            print("Eixo X")
    elif ponto[0] < 0:
        if ponto[1] > 0:
            print("Q2")
        elif ponto[1] < 0:
            print("Q3")
        else:
            print("Eixo X")
    else:
        if ponto[1] != 0:
            print("Eixo Y")
        else:
            print("Origem")


if __name__ == "__main__":
    coordenada = [float(entrada) for entrada in input().split()]
    classifica_ponto(coordenada)
