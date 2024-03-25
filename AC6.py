def exercicio_1010():
    peca1 = input()
    peca2 = input()

    peca1 = peca1.split(" ")
    peca2 = peca2.split(" ")

    peca1[0] = int(peca1[0])
    peca1[1] = int(peca1[1])
    peca1[2] = float(peca1[2])

    peca2[0] = int(peca2[0])
    peca2[1] = int(peca2[1])
    peca2[2] = float(peca2[2])

    total_1 = peca1[1] * peca1[2]
    total_2 = peca2[1] * peca2[2]

    total_3 = total_1 +total_2
    print(f"VALOR A PAGAR: R$ {total_3:.2f}")

def exercicio_1000():
    print("Hello World!")

def exercicio_1001():
    valor_1 = int(input())
    valor_2 = int(input())
    total = valor_1 * valor_2
    print("X =", total)

def exercicio_1013():
    valores = input()
    valores = valores.split(" ")

    valores[0] = int(valores[0])
    valores[1] = int(valores[1])
    valores[2] = int(valores[2])

    calculo_ab = (valores[0] + valores[1] + abs(valores[0] - valores[1]))/2
    if calculo_ab < valores[2]:
        print(f"{valores[2]} eh o maior")
    else:
        print(f"{int(calculo_ab)} eh o maior")

def exercicio_1015():
    coordenada_1 = input()
    coordenada_2 = input()

    coordenada_1 = coordenada_1.split(" ")
    coordenada_2 = coordenada_2.split(" ")

    coordenada_1[0] = float(coordenada_1[0])
    coordenada_1[1] = float(coordenada_1[1])

    coordenada_2[0] = float(coordenada_2[0])
    coordenada_2[1] = float(coordenada_2[1])

    distancia = ((coordenada_2[0] - coordenada_1[0])**2 + (coordenada_2[1] - coordenada_1[1])**2)**(1/2)
    print(f"{distancia:.4f}")