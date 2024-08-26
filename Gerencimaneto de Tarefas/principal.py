import mysql.connector
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate

valor_id = 0

# Configuração da conexão com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ap112233$",
    database="gerenciador_tarefas"
)
#Configuração da tela principal
def funcao_principal():
    descricao = formulario.lineEdit.text()
    data_criacao = formulario.dateEdit.text()
    data_conclusao = formulario.dateEdit_2.text()
    autor = formulario.lineEdit_4.text()
#Conexão com o banco de dados
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO gerenciador_tarefas (descricao, data_criacao, data_conclusao, autor) VALUES (%s, %s, %s, %s)"
    dados = (descricao, data_criacao, data_conclusao, autor)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    
    # Limpar campos do formulário
    formulario.lineEdit.setText("")
    formulario.dateEdit.setDate(QDate(2000, 1, 1))
    formulario.dateEdit_2.setDate(QDate(2000, 1, 1))
    formulario.lineEdit_4.setText("")

#Configuração da tela de listar dados
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM gerenciador_tarefas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#Excluir tarefa
def excluir_tarefa():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM gerenciador_tarefas")
    dados_lidos = cursor.fetchall()
    id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM gerenciador_tarefas WHERE id = {}".format(id))

#Editar tarefa
def chama_editar_tarefa():
    global valor_id
    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM gerenciador_tarefas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM gerenciador_tarefas WHERE id="+ str(valor_id))
    tarefa = cursor.fetchall()
    editar_tarefa.show()
#Salvar dados editados
def salvar_dados_editados():
    #Pega o id
    global valor_id
    descricao = editar_tarefa.lineEdit.text()
    data_criacao = editar_tarefa.dateEdit.text()
    data_conclusao = editar_tarefa.dateEdit_2.text()
    autor = editar_tarefa.lineEdit_4.text()
    print(descricao, autor)
    #Atulizar dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE gerenciador_tarefas SET descricao = '{}', data_criacao = '{}', data_conclusao = '{}', autor = '{}' WHERE id = {}".format(descricao, data_criacao, data_conclusao, autor, valor_id))
    banco.commit()
    #Atualizar dados na listagem
    editar_tarefa.close()
    segunda_tela.close()
    chama_segunda_tela()
    

# Configuração da aplicação PyQt
app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
editar_tarefa = uic.loadUi("editar_tarefa.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_tarefa)
segunda_tela.pushButton_2.clicked.connect(chama_editar_tarefa)
editar_tarefa.pushButton.clicked.connect(salvar_dados_editados)


formulario.show()
app.exec()
