#1-

def determina_tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return print("Triângulo Equilatero! ")
        elif a == b or a == c or b == c:
            return print("Triângulo Isósceles!")
        else:
            return print("Triângulo Escaleno!")
    else:
        return print("Não é um Triângulo!" )
    
determina_tipo_triangulo(2,2,10)


#2-

def dia_semana(num):
   if num == 1:
       return "Domingo"
   if num == 2:
       return "Segunda-feira"
   if num == 3:
       return "Twrça-feira"   
   if num == 4: 
       return "Quarta-feira"
   if num == 5:
       return "Quinta-feira"
   if num == 6:
       return "Sexta-feira"
   if num == 7:
       return "Sábado"
   
   if num > 7 and num < 1:
    return "Número Inválido"
   
print(dia_semana(5))


#3-

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplica(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculadora():
    x = input("Informe seu nome: ")
    
    print("Olá, bem vindo a Calculadora",x)

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número:"))
    operacao = input("Informe qual operação desejada: ")

    if operacao == "soma":
        resultado = print(soma(num1, num2))
    elif operacao == "subtracao":
        resultado = print(subtracao(num1,num2))
    elif operacao == "divide":
        resultado = print(divide(num1,num2))
    elif operacao == "multiplica":
        resultado = print(multiplica(num1,num2))
    else:
        print("Operação Inválida")

calculadora()
