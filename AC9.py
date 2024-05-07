"""
AC9-
"""


#1016-

km = int(input())
tempo = km * 2
print(tempo, "minutos")

#1153-

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

n = int(input())

if 0 < n < 13:
    resultado = calcular_fatorial(n)
    print(resultado)
else:
    print("O número inserido está fora do intervalo permitido.")


#1281-

n = int(input())
while n:
    n -= 1
    feira = {}
    final = 0.0

    m = int(input())
    while m:
        m -= 1
        item, valor = input().split()
        feira[item] = float(valor)

    p = int(input())
    while p:
        p -= 1
        item, qt = input().split()
        final += feira[item] * int(qt)

    print('R$ %.2f' % final)

#2006-

tipo_cha_real = int(input())


respostas = list(map(int, input().split()))

corretas = 0
for resposta in respostas:
    if resposta == tipo_cha_real:
        corretas += 1

print(corretas)


#2339-

lista = input()
lista = lista.split(" ")
c = int(lista[0])
p = int(lista[1])
f = int(lista[2])
if c * f <= p:
    print("S")
else:
    print("N")


#2388-

def calcular_distancia(tempo, velocidade):
    return tempo * velocidade

def calcular_distancia_total(intervalos):
    distancia_total = 0
    for intervalo in intervalos:
        tempo, velocidade = intervalo
        distancia_total += calcular_distancia(tempo, velocidade)
    return distancia_total

N = int(input())

intervalos = []

for _ in range(N):
    tempo, velocidade = map(int, input().split())
    intervalos.append((tempo, velocidade))

distancia_total = calcular_distancia_total(intervalos)

print(distancia_total)


#2413-

t = int(input())

print(4 * t)


#3048-

lista = []

for _ in range (int(input())):
    number = input()
    if not lista:
        lista.append(number)
    elif number != lista [-1]:
        lista.append(number)

print(len(lista))