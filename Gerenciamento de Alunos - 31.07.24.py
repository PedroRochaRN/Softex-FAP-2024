def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    curso = input("Digite o curso do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno: "))
        notas.append(nota)
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso,
        "notas": notas
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Matrícula:", aluno["matricula"])
        print("Curso:", aluno["curso"])
        print("Notas:", aluno["notas"])
        media = sum(aluno["notas"]) / len(aluno["notas"])
        print("Média:", media)
        print()

def editar_aluno(alunos):
    matricula = input("Digite a matrícula do aluno que deseja editar: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            nome = input("Digite o novo nome do aluno: ")
            curso = input("Digite o novo curso do aluno: ")
            notas = []
            for i in range(4):
                nota = float(input(f"Digite a nova nota {i+1} do aluno: "))
                notas.append(nota)
            aluno["nome"] = nome
            aluno["curso"] = curso
            aluno["notas"] = notas
            print("Aluno editado com sucesso!")
            return
    print("Aluno não encontrado.")

def excluir_aluno(alunos):
    matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("Aluno excluído com sucesso!")
            return
    print("Aluno não encontrado.")

def calcular_media(alunos):
    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        print("Matrícula:", aluno["matricula"])
        print("Média:", media)
        print()

def menu():
    alunos = []
    while True:
        print("----- Sistema de Gerenciamento de Alunos -----")
        print("1 - Cadastrar novo aluno")
        print("2 - Listar todos os alunos cadastrados")
        print("3 - Editar informações de um aluno")
        print("4 - Excluir um aluno do sistema")
        print("5 - Calcular e exibir a média das notas de cada aluno")
        print("0 - Sair do programa")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            editar_aluno(alunos)
        elif opcao == "4":
            excluir_aluno(alunos)
        elif opcao == "5":
            calcular_media(alunos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")

menu()