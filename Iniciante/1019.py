segundos = int(input())
minutos = 0
horas = 0

if segundos >= 60:
    minutos = int(segundos / 60)
    segundos %= 60
    if minutos >= 60:
        horas = int(minutos / 60)
        minutos %= 60

print('{}:{}:{}'.format(horas, minutos, segundos))
