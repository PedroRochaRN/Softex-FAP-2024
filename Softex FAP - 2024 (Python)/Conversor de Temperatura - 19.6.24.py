# O sistema irá perguntar se você utiliza Celsius ou Fahrenheit.
# Se escolher Celsius, você deve informar a temperatura em Celsius e o sistema calculará e mostrará a temperatura equivalente em Fahrenheit.
# Se escolher Fahrenheit, você deve informar a temperatura em Fahrenheit e o sistema calculará e mostrará a temperatura equivalente em Celsius.


while True:

    escolha = input("Digite 1 para converter de Celsius para Fahrenheit ou 2 para converter de Fahrenheit para Celsius: ")
    
    if escolha not in ["1","2"]:
        print("Entrada inválida. Insira valores numéricos.")
        continue
    
    if escolha == "1":
        while True:
            try:
                C = float(input("Digite a temperatura em Celsius para converter para Fahrenheit: "))
                F = (C * 9/5) + 32
                print(f"A temperatura em Fahrenheit é de {F:.2f}°F.")
                break
            except ValueError:
                print("Entrada inválida. Insira valores numéricos para a temperatura.")

    elif escolha == "2":
        while True:
            try:
                F = float(input("Digite a temperatura em Fahrenheit para converter para Celsius: "))
                C = (F - 32) * 5/9
                print(f"A temperatura em Celsius é de {C:.2f}°C.")
                break
            except ValueError:
                print("Entrada inválida. Insira valores numéricos para a temperatura.")
        
    break