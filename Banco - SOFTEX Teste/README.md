# 💼💳 Sistema Bancário - Teste Softex

Projeto de sistema bancário desenvolvido em Python com banco de dados do MySQL, possui interface interativa desenvolvida em PyQt5. O projeto possibilita cadastrar clientes, listar, editar, sacar, etc.

## ▶ Demonstração





[![Veja o vídeo](https://img.youtube.com/vi/T-D1KVIuvjA/maxresdefault.jpg)](https://youtu.be/pQpFwH5KHvo)





## Funcionalidades 🛠️

### Cadastro de Clientes 👤

A função para registrar clientes, integra a janela interativa, `formulario.ui` com o banco de dados, o usuário deverá inserir o seu Nome, a Data atual e o Saldo (Caso não tenha saldo inicial, colocar 0). A tabela também conta com `ID`, mas o mesmo é gerado automaticamente. Após preencher os dados, o usuário deverá clicar em "Inserir" no menu interativo e as informações serão inseridas na tabela `dados`.

### Listagem 📋

A função para listar dados, integra a janela interativa, `listar_dados.ui` com o banco de dados, ao clicar no botão `Listar` na janela do `formulário.ui`, abrirá a janela do `listar_dados.ui`. Ela lê a tabela `dados` e insere as informações no widget de tabela. 

### Excluir 🗑️

A função para excluir tarefa, integra a janela interativa, `listar_dados.ui` com o banco de dados, ela lê a tabela `dados` e ao selecionar a coluna no menu interativo, irá pegar o ID único e ao pressionar o botão `excluir`, todas as informações selecionadas serão apagadas da tabela `dados`.

### Editar 🖌️

A função para editar tarefa, integra a janela interativa, `editar_tarefa.ui` com o banco de dados, ao selecionar a coluna desejada e clicar no botão `Editar` na janela `listar_dados.ui`, com base no `ID`, abrirá a janela do `editar_tarefa`, assim lendo a tabela.

### Salvar dados editados 🖌️

A função para salvar dados editados, integra a janela interativa, `editar_tarefa.ui` com o banco de dados, com base no `ID`, o usuário poderá editar todas as informações atreladas com base no `ID`, exceto o `ID`, ao clicar no botão `Salvar`, a função executará um comando para editar dos dados solicitados na tabela.

### Saque 💸 e Deposito 💳

A função para realizar a operação, integra a janela interativa, `carteira.ui` com o banco de dados, ao clicar no botão `Carteira` na janela do `formulario.ui`, abrirá a janela `carteira.ui`. O usuário deverá inserir um `ID` já existente, junto com o `Valor` desejado e selecionar se deseja sacar ou depositar esse `Valor`. Caso o usuário não colocar `ID`, `Valor` ou não marcar uma ação desejada, o menu interativo apresentará uma mensagem de erro, caso o valor de saque exceda o `valor` do `saldo`, também será executado um erro. Ao clicar no botão `Confirmar`, caso seja marcado `Depósito` no menu interativo, ele executará, uma soma do `valor` com a do `Saldo`, e atualizará o saldo na tabela `dados`, caso o usuário marque `Saque`, o programa executará uma subtração do `Valor` e do `Saldo`. Em ambas as situações o programa irá inserir todas as informações (ID, Nome, Data_Criacao, Saldo) numa nova tabela chamada `extrato`.

### Extrato 📝

A função para exibir o extrato, integra a janela interativa, `extratos.ui` com o banco de dados, ao clicar no botão `Extrato` na janela do `formulario.ui`, abrirá a janela `extratos.ui`. A função funciona da mesma maneira que a função de `listar dados`, a única diferença é que em vez de ler a tabela `dados`, ela lê a tabela `extrato`.

## Uso 🚀
### 1° Parte, conexão com MySQL -
Após conectar o MySQL com o editor de sua prefência, será necessário criar a Database e as tabelas de fato, todos os códigos necessários poderão ser encontrados no arquivo `Query (.sql`, basta executa-los. 

### 2° Parte, execução -
O programa principal está no arquivo `principal.py`, será necessário alterar informações para que ocorra a conexão do banco de dados, se encontra a partir da linha 7 do arquivo, após isso instale as dependências e execute o código.

## Dependências 🔧

Este projeto utiliza as bibliotecas `mysql.connector` para a integração com o banco de dados e `PyQt5` para que o menu interativo funcione. Para instalar essas bibliotecas, execute o seguinte comando no terminal:

```
pip install mysql-connector-python
pip install pyqt5 

```

