def bhaskara():
    a=int(input("Informe A: "))
    b=int(input("Informe B: "))
    c=int(input("Informe C: "))

    res1 = (-b+((b**2 -4*a*c)**(1/2)))/(2*a)
    res2 = (-b-((b**2 -4*a*c)**(1/2)))/(2*a)
    
    print("Resultado 1,", res1)
    print("Resultado 2,", res2)
    
    return(res1, res2)

bhaskara()



def ano_bi():
    ano = int(input("Informe o Ano: "))

    res=((ano % 4)==0 and ((ano%400==0)or not (ano%100==0)))

    print("Resultado:", res)
    
ano_bi()