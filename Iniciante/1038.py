def calcula_pedido(codigo: int, quantidade: int):
    if codigo == 1:
        return float(quantidade * 4.0)
    elif codigo == 2:
        return float(quantidade * 4.5)
    elif codigo == 3:
        return float(quantidade * 5)
    elif codigo == 4:
        return float(quantidade * 2)
    elif codigo == 5:
        return float(quantidade * 1.5)


if __name__ == "__main__":
    cod, quant = [float(entrada) for entrada in input().split()]
    print("Total: R$ {0:.2f}".format(calcula_pedido(cod, quant)))
