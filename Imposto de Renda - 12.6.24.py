while True:
    X = float(input("Insira seu salário: R$"))
    if X <= 2259.20:
        print ("Isento")
    elif X <= 2826.65:
        imposto = ( X * 0.075 ) - 169.44
        print (f"Seu imposto é de R${imposto:.2f}")
    elif X <= 3751.05:
        imposto = (X * 0.15) - 381.44
        print (f"Seu imposto é de R${imposto:.2f}")
    elif X <= 4664.68:
        imposto = (X * 0.225) - 662.77
        print (f"Seu imposto é de R$ {imposto:.2f}")
    else:
        imposto = (X * 0.275) - 896.00
        print (f"Seu imposto é de R$ {imposto:.2f}" ) 
    break