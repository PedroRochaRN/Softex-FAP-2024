import mysql.connector
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate
from datetime import datetime

valor_id = 0

# Configuração da conexão com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0909",
    database="banco"
)

# Função para registrar clientes
def funcao_principal():
    nome = formulario.lineEdit.text()
    data_criacao = datetime.now().strftime('%Y-%m-%d')  # Usando data atual
    saldo = formulario.lineEdit_4.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO dados (nome, data_criacao, saldo) VALUES (%s, %s, %s)"
    dados = (nome, data_criacao, saldo)
    cursor.execute(comando_SQL, dados)
    banco.commit()

    # Limpar campos do formulário
    formulario.lineEdit.setText("")
    formulario.lineEdit_4.setText("")

# Função para listar dados
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM dados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# Função para excluir tarefa
def excluir_tarefa():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM dados WHERE id = %s", (id,))
    banco.commit()

# Editar tarefa
def chama_editar_tarefa():
    editar_tarefa.show()
    global valor_id
    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM dados WHERE id="+ str(valor_id))
    tarefa = cursor.fetchall()

# Salvar dados editados
def salvar_dados_editados():
    # Pega o id
    global valor_id
    # Integração com o aplicativo
    nome = editar_tarefa.lineEdit.text()
    data_criacao = datetime.now().strftime('%Y-%m-%d')  # Usando data atual
    saldo = editar_tarefa.lineEdit_4.text()
    # Atualizar dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE dados SET nome = %s, data_criacao = %s, saldo = %s WHERE id = %s", 
                   (nome, data_criacao, saldo, valor_id))
    banco.commit()
    # Atualizar dados na listagem
    editar_tarefa.close()
    segunda_tela.close()
    chama_segunda_tela()

# Configuração da tela de saque e depósito
def chama_carteira():
    carteira.show()

# Função para realizar saque e depósito e atualizar a tabela de extrato
def realizar_operacao():
    try:
        id_usuario = carteira.lineEdit.text()
        valor = float(carteira.lineEdit_2.text())

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero")

        cursor = banco.cursor()
        
        # Verificar se o ID do usuário existe na tabela dados
        cursor.execute("SELECT saldo, nome, data_criacao FROM dados WHERE id = %s", (id_usuario,))
        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError("ID não encontrado")

        saldo_atual, nome, data_criacao = resultado

        if carteira.radioButton.isChecked():  # Depósito
            novo_saldo = saldo_atual + valor
        elif carteira.radioButton_2.isChecked():  # Saque
            if valor > saldo_atual:
                raise ValueError("Saldo insuficiente")
            novo_saldo = saldo_atual - valor
        else:
            raise ValueError("Nenhuma operação selecionada")

        # Atualizar saldo na tabela dados
        cursor.execute("UPDATE dados SET saldo = %s WHERE id = %s", (novo_saldo, id_usuario))
        
        # Inserir registro na tabela extrato
        comando_SQL = "INSERT INTO extrato (id, nome, data_criacao, saldo) VALUES (%s, %s, %s, %s)"
        dados_extrato = (id_usuario, nome, data_criacao, novo_saldo)
        cursor.execute(comando_SQL, dados_extrato)
        banco.commit()

        # Limpar campos da tela de carteira
        carteira.lineEdit.setText("")
        carteira.lineEdit_2.setText("")

    except ValueError as e:
        QtWidgets.QMessageBox.warning(carteira, "Erro", str(e))
    except mysql.connector.Error as e:
        QtWidgets.QMessageBox.warning(carteira, "Erro do Banco de Dados", str(e))
    except Exception as e:
        QtWidgets.QMessageBox.warning(carteira, "Erro", str(e))



# Função para exibir extrato
def chama_extrato():
    extratos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM extrato"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    extratos.tableWidget.setRowCount(len(dados_lidos))
    extratos.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            extratos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# Configuração da aplicação PyQt
app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
editar_tarefa = uic.loadUi("editar_tarefa.ui")
extratos = uic.loadUi("extratos.ui")
carteira = uic.loadUi("carteira.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.pushButton_3.clicked.connect(chama_extrato)
formulario.pushButton_4.clicked.connect(chama_carteira)
segunda_tela.pushButton.clicked.connect(excluir_tarefa)
segunda_tela.pushButton_2.clicked.connect(chama_editar_tarefa)
editar_tarefa.pushButton.clicked.connect(salvar_dados_editados)
carteira.pushButton_3.clicked.connect(realizar_operacao)  

formulario.show()
app.exec()
