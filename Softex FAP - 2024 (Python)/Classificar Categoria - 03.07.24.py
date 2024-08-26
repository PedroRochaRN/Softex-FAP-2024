def classificar_idade(idade):
    if idade < 13:
        return "Criança"
    elif 13 <= idade < 18:
        return "Adolescente"
    elif 18 <= idade < 60:
        return "Adulto"
    else:
        return "Idoso"

# Exemplo de uso
idades = [4, 15, 22, 67, 45, 12]
categorias = [classificar_idade(idade) for idade in idades]

print(categorias)
