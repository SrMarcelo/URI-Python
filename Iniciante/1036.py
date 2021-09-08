a, b, c = [float(i) for i in input().split()]

delta = (b ** 2) - (4 * a * c)

if a == 0 or delta < 0:
    print('Impossivel calcular')

else:
    R1 = (-b + (delta ** (1 / 2))) / (2 * a)
    R2 = (-b - (delta ** (1 / 2))) / (2 * a)
    print('R1 = {0:.5f}'.format(R1))
    print('R2 = {0:.5f}'.format(R2))
