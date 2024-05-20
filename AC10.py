#1258-

class Camiseta:
    def __init__(self, n, c, t):
        self.nome = n
        self.cor = c
        self.tamanho = t


def comp(a, b):
    if(a.cor == b.cor):
        if(a.tamanho == b.tamanho):
            if(a.nome < b.nome):
                return -1
            if(a.nome > b.nome):
                return 1
            return 0
        if(a.tamanho > b.tamanho):
            return -1
        return 1
    if(a.cor < b.cor):
        return -1
    return 1


def particao(V, inicio, fim):
    pivo = V[fim - 1]
    i = inicio
    for j in range(inicio, fim):
        if(comp(V[j], pivo) < 0):
            V[j], V[i] = V[i], V[j]
            i += 1

    if(comp(pivo, V[i]) < 0):
        V[fim - 1], V[i] = V[i], V[fim - 1]

    return i


def quickSort(V, inicio, fim):
    if(fim > inicio):
        posicaoPivo = particao(V, inicio, fim)
        quickSort(V, inicio, posicaoPivo)
        quickSort(V, posicaoPivo + 1, fim)


first = True
while True:
    try:
        N = int(input())

        if(N == 0):
            break

        if(first):
            first = False
        else:
            print('')

        camisetas = []
        for _ in range(N):
            nome = input()
            cor, tamanho = input().strip().split(' ')

            camisetas.append(Camiseta(nome, cor, tamanho))

        quickSort(camisetas, 0, len(camisetas))

        for camiseta in camisetas:
            print(f'{camiseta.cor} {camiseta.tamanho} {camiseta.nome}')
    except EOFError:
        break





#1260-

import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    index = 0
    cases = int(data[index])
    index += 1
    
    for case in range(cases):
        if case > 0:
            print()
        
        avres = defaultdict(int)
        total = 0
        
        while index < len(data) and data[index].strip() == '':
            index += 1
        
        while index < len(data) and data[index].strip() != '':
            avre = data[index].strip()
            avres[avre] += 1
            total += 1
            index += 1
        
        for tree in sorted(avres):
            percentage = (avres[tree] / total) * 100
            print(f"{tree} {percentage:.4f}")

if __name__ == "__main__":
    main()





#2518-

import math
import sys

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    index = 0
    while index < len(data):
        N = int(data[index])
        index += 1
        H, C, L = map(int, data[index].split())
        index += 1
    
        altura_total = N * H
        comprimento_total = N * C
        hipotenusa = math.sqrt(altura_total ** 2 + comprimento_total ** 2)
        
        area_cm2 = hipotenusa * L
        
        area_m2 = area_cm2 / 10000
        
        print(f"{area_m2:.4f}")

if __name__ == "__main__":
    main()
