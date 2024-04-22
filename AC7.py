#1-

salario = float(input())


percentual_reajuste = 0

if salario <= 400:
    percentual_reajuste = 15
elif salario <= 800:
    percentual_reajuste = 12
elif salario <= 1200:
    percentual_reajuste = 10
elif salario <= 2000:
    percentual_reajuste = 7
else:
    percentual_reajuste = 4

reajuste = salario * (percentual_reajuste / 100)
novo_salario = salario + reajuste


print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual_reajuste} %")


#2-


quantidade_pares = 0

valores = [int(input()) for _ in range(5)]


for valor in valores:
    if valor % 2 == 0:
        quantidade_pares += 1


print(quantidade_pares, "valores pares")

#3- 
x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0

for num in range(x, y + 1):
  
    if num % 13 != 0:
        
        soma += num


print(soma)

#4-


v = int(input())

n = [0] * 10

n[0] = v

for i in range(1, 10):
    n[i] = n[i - 1] * 2

for i in range(10):
    print("N[" + str(i) + "] = " + str(n[i]))

#5-


n = int(input())

x = list(map(int, input().split()))

menor_valor = x[0]
posicao = 0

for i in range(1, n):
    if x[i] < menor_valor:
        menor_valor = x[i]
        posicao = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao)

#6 e 7 não consegui fazer...


