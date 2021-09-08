dinheiro = float(input())

nota100, nota50, nota20, nota10, nota5, nota2 = [0] * 6

moeda1, moeda050, moeda025, moeda010, moeda005, moeda001 = [0] * 6

nota100 = int(dinheiro/100)
dinheiro %= 100

nota50 = int(dinheiro/50)
dinheiro %= 50

nota20 = int(dinheiro/20)
dinheiro %= 20

nota10 = int(dinheiro/10)
dinheiro %= 10

nota5 = int(dinheiro/5)
dinheiro %= 5

nota2 = int(dinheiro/2)
dinheiro %= 2

moeda1 = int(dinheiro/1)
dinheiro %= 1

moeda050 = int(dinheiro/0.5)
dinheiro %= 0.5

moeda025 = int(dinheiro/0.25)
dinheiro %= 0.25

moeda010 = int(dinheiro/0.1)
dinheiro %= 0.1

moeda005 = int(dinheiro/0.05)
dinheiro %= 0.05

moeda001 = int(dinheiro/0.01 + 0.1)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(nota100))
print('{} nota(s) de R$ 50.00'.format(nota50))
print('{} nota(s) de R$ 20.00'.format(nota20))
print('{} nota(s) de R$ 10.00'.format(nota10))
print('{} nota(s) de R$ 5.00'.format(nota5))
print('{} nota(s) de R$ 2.00'.format(nota2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(moeda1))
print('{} moeda(s) de R$ 0.50'.format(moeda050))
print('{} moeda(s) de R$ 0.25'.format(moeda025))
print('{} moeda(s) de R$ 0.10'.format(moeda010))
print('{} moeda(s) de R$ 0.05'.format(moeda005))
print('{} moeda(s) de R$ 0.01'.format(moeda001))

