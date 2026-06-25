# Gerenciador de Tarefas

Um projeto de gerenciamento de tarefas diárias, desenvolvido em Python utilizando a biblioteca **CustomTkinter**.

## Funcionalidades

* **Adicionar Tarefas:** Digite o nome da tarefa e clique em "Adicionar" ou simplesmente aperte **Enter**.
* **Concluir Tarefas:** Digite o número da tarefa desejada para marcá-la com um indicador `[X]` visual.
* **Remover Tarefas:** Digite o número da tarefa para excluí-la definitivamente da lista.
* **Persistência de Dados (Salvamento Automático):** Suas tarefas são salvas automaticamente em um arquivo local (`tarefas.json`). Você pode fechar o aplicativo e reabri-lo sem perder nenhuma informação.
* **Interface Moderna:** Sistema visual com suporte nativo a rolagem para listas grandes (Scrollable Frame) e tratamento de erros com alertas visuais (`messagebox`).



## Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **JSON** (Módulo nativo do Python para armazenamento local de dados)
* **OS** (Módulo nativo do Python para manipulação de arquivos do sistema)
* Tkinter / Messagebox (Tratamento de alertas nativos)


## Como Executar o Projeto
1. Certifique-se de ter o Python instalado na sua máquina.

2. Baixe o arquivo do projeto e abra o terminal na pasta dele.

3. Instalar as dependências.
```bash
pip install customtkinter
```
4. Executar o arquivo.
```bash
python crud.py
```
