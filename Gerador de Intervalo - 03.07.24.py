def intervalo(inicio, fim, passo=1):
    atual = inicio
    while atual < fim:
        yield atual
        atual += passo

# Exemplo de uso
for numero in intervalo(1, 10, 2):
    print(numero)
