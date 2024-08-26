while True:
    try:
        Peso = float(input("Insira seu peso em quilogramas: "))
        Altura = float(input("Insira sua altura em metros: "))
    except ValueError:
        print("Entrada inválida. Insira valores numéricos.")
        continue
    
    if Peso <= 0 or Altura <= 0:
        print("Insira valores válidos maiores que zero.")
        continue

    imc = Peso / (Altura ** 2)

    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 34.9:
        categoria = "Obesidade Grau 1"
    elif imc < 39.9:
        categoria = "Obesidade Grau 2"
    else:
        categoria = "Obesidade Grau 3"

    print(f"Seu IMC é {imc:.2f}, o que te classifica como: {categoria}.")
    break