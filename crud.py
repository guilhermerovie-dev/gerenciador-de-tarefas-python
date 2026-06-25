import customtkinter as ctk
from tkinter import messagebox
import json
import os

ARQUIVO_SALVAMENTO = "tarefas.json"
lista = []

def salvar_tarefas():
    with open(ARQUIVO_SALVAMENTO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

def carregar_tarefas():
    global lista
    if os.path.exists(ARQUIVO_SALVAMENTO):
        try:
            with open(ARQUIVO_SALVAMENTO, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
        except:
            lista = []

def atualizar_lista_tarefas():
    for componente in frame_tarefas.winfo_children():
        componente.destroy()
    
    for indice, item in enumerate(lista, start=1):
        texto_formatado = f"{indice}. {item['titulo']}"
        if item["concluido"]:
            texto_formatado += " [OK]"
            
        label_tarefa = ctk.CTkLabel(
            frame_tarefas, 
            text=texto_formatado, 
            font=("Arial", 14, "bold"),
            text_color="gray" if item["concluido"] else None
        )
        label_tarefa.pack(pady=5, anchor="w")

def adicionar_tarefa(event=None):
    texto_tarefa = entrada_tarefa.get().title().strip()
    if not texto_tarefa:
        return
    
    lista.append({"titulo": texto_tarefa, "concluido": False})
    entrada_tarefa.delete(0, "end")
    salvar_tarefas()
    atualizar_lista_tarefas()

def processar_tarefa(acao):
    valor_digitado = entrada_tarefa.get().strip()
    try:
        indice_real = int(valor_digitado) - 1
        if acao == "concluir":
            lista[indice_real]["concluido"] = True
        elif acao == "remover":
            lista.pop(indice_real)
            
        entrada_tarefa.delete(0, "end")
        salvar_tarefas()
        atualizar_lista_tarefas()
    except (ValueError, IndexError):
        messagebox.showerror("Erro", "Digite o número correto da tarefa na barra de texto.")



ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x550")
janela.resizable(False, False)

fonte_negrito = ctk.CTkFont(weight="bold")
titulo = ctk.CTkLabel(janela, text="Minhas Tarefas", font=("Arial", 22, "bold"))
titulo.pack(pady=15)

entrada_tarefa = ctk.CTkEntry(janela, placeholder_text="Digite a tarefa ou o número para ação...", width=300, font=("Arial", 14))
entrada_tarefa.bind("<Return>", adicionar_tarefa)
entrada_tarefa.pack(pady=10)

# Botões 
btn_add = ctk.CTkButton(janela, text="Adicionar Tarefa", command=adicionar_tarefa, width=300, fg_color="green", hover_color="darkgreen", font=fonte_negrito)
btn_add.pack(pady=5)



# Frame botões 
frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(pady=5)

btn_concluir = ctk.CTkButton(frame_botoes, text="Concluir", command=lambda: processar_tarefa("concluir"), width=145, font=fonte_negrito)
btn_concluir.pack(side="left", padx=5)

btn_remover = ctk.CTkButton(frame_botoes, text="Remover", command=lambda: processar_tarefa("remover"), width=145, fg_color="red", hover_color="darkred", font=fonte_negrito)
btn_remover.pack(side="right", padx=5)

frame_tarefas = ctk.CTkScrollableFrame(janela, width=350, height=250)
frame_tarefas.pack(pady=15)

carregar_tarefas()
atualizar_lista_tarefas()
janela.mainloop()
