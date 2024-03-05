
def usuario():
    return input("Informe seu nome:" )

def nota():
    a1 = float(input("Informe a nota da A1:" ))
    a2 = float(input("Informe a nota da A2:" ))
    asub = float(input("Informe a nota da AS:" ))
    ac = float(input("Informe a nota da AC:" ))
    return a1, a2, asub, ac

def validar_notas(a1, a2, asub, ac):
    if a1>10 or a1<0:
        return False
    if a2>10 or a2<0:
        return False
    if asub>10 or asub<0:
        return False
    if ac>10 or ac<0:
        return False
    else:
        return True

def maiores_notas(a1,a2,asub):
    if a1<asub :
        return asub, a2
    if a2<asub:
        return asub, a1
    return a1, a2

def calculo_media(a1, a2,ac):
    return (a1 + a2) * 0.4 + ac * 0.2


def aprovacao(calculo_media):
    print("Sua média foi de: ", round(calculo_media))
    if calculo_media >= 7:
        print("Aprovado!!")
    else:
        print("Reprovado")


def main():
    nome = usuario()

    if nome:
        a1,a2,asub,ac = nota()
    if validar_notas(a1,a2,asub,ac):
        a1,a2 = maiores_notas(a1,a2,asub)
        media = calculo_media(a1, a2, ac)
        aprovacao(media)

main()



