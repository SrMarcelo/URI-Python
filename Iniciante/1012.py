A, B, C = [float(i) for i in input().split()]

areaTriangulo = (A * C) / 2
areaCirculo = 3.14159 * (C ** 2)
areaTrapezio = ((A + B) * C) / 2
areaQuadrado = B ** 2
areaRetangulo = A * B

print("TRIANGULO: {0:.3f}".format(areaTriangulo))
print("CIRCULO: {0:.3f}".format(areaCirculo))
print("TRAPEZIO: {0:.3f}".format(areaTrapezio))
print("QUADRADO: {0:.3f}".format(areaQuadrado))
print("RETANGULO: {0:.3f}".format(areaRetangulo))