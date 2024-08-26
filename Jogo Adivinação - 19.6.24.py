import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    
    print("Tente adivinhar o número secreto entre 0 e 100.")
    
    while True:
        try:
            chute = int(input("Digite um número: "))
            tentativas += 1
            
            if chute < numero_secreto:
                print(f"O número secreto é maior. Tentativas até então: {tentativas}")
            elif chute > numero_secreto:
                print(f"O número secreto é menor. Tentativas até então: {tentativas}")
            else:
                print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativa(s).")
                break
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    print("Fim do jogo!")


jogo_adivinhacao()