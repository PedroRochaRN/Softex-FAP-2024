from tabulate import tabulate

crimes = {}
suspeitos = {}
evidencias = {}

# Função para adicionar um crime
def adicionar_crime():
    crime = {}
    crime_id = int(input("ID do crime: "))
    
    crime["descricao"] = input("Descrição do crime: ")
    crime["local"] = input("Local do crime: ")
    crime["data"] = input("Data do crime (DD/MM/AAAA): ")
    
    crimes[crime_id] = crime

# Função para adicionar um suspeito
def adicionar_suspeito():
    suspeito = {}
    suspeito_id = int(input("ID do suspeito: "))
    
    suspeito["nome"] = input("Nome do suspeito: ")
    suspeito["idade"] = int(input("Idade do suspeito: "))
    suspeito["sexo"] = input("Sexo do suspeito (M/F): ")
    suspeito["endereco"] = input("Endereço do suspeito: ")
    
    suspeitos[suspeito_id] = suspeito

# Função para adicionar uma evidência
def adicionar_evidencia():
    evidencia = {}
    evidencia_id = int(input("ID da evidência: "))
    
    evidencia["descricao"] = input("Descrição da evidência: ")
    evidencia["crime_id"] = int(input("ID do crime relacionado: "))
    
    evidencias[evidencia_id] = evidencia

# Função para listar crimes
def listar_crimes():
    if not crimes:
        print("Nenhum crime registrado.")
        return
    
    data = [[crime_id, crime["descricao"], crime["local"], crime["data"]] for crime_id, crime in crimes.items()]
    print(tabulate(data, headers=["ID", "Descrição", "Local", "Data"], tablefmt="simple_grid"))

# Função para listar suspeitos
def listar_suspeitos():
    if not suspeitos:
        print("Nenhum suspeito registrado.")
        return
    
    data = [[suspeito_id, suspeito["nome"], suspeito["idade"], suspeito["sexo"], suspeito["endereco"]] for suspeito_id, suspeito in suspeitos.items()]
    print(tabulate(data, headers=["ID", "Nome", "Idade", "Sexo", "Endereço"], tablefmt="simple_grid"))

# Função para listar evidências
def listar_evidencias():
    if not evidencias:
        print("Nenhuma evidência registrada.")
        return
    
    data = [[evidencia_id, evidencia["descricao"], evidencia["crime_id"]] for evidencia_id, evidencia in evidencias.items()]
    print(tabulate(data, headers=["ID", "Descrição", "ID do Crime"], tablefmt="simple_grid"))

# Menu principal
while True:
    print("\n[1] Adicionar Crime")
    print("[2] Adicionar Suspeito")
    print("[3] Adicionar Evidência")
    print("[4] Listar Crimes")
    print("[5] Listar Suspeitos")
    print("[6] Listar Evidências")
    print("[0] Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        adicionar_crime()
    elif escolha == 2:
        adicionar_suspeito()
    elif escolha == 3:
        adicionar_evidencia()
    elif escolha == 4:
        listar_crimes()
    elif escolha == 5:
        listar_suspeitos()
    elif escolha == 6:
        listar_evidencias()
    elif escolha == 0:
        break
    else:
        print("Opção inválida.")
