import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
lista = []

def atualizar_lista_tarefas():
    for componente in frame_tarefas.winfo_children():
        componente.destroy()
    

    for indice, item in enumerate(lista, start=1):
        if item["concluido"] == False:
            texto_formatado = f"{indice}. {item['titulo']}"
            label_tarefa = ctk.CTkLabel(frame_tarefas, text=texto_formatado, font=("Arial", 14, "bold"))
            label_tarefa.pack(pady=5, anchor="w")
        else:
            texto_formatado = f"{indice}. {item['titulo']} | [X]"
            label_tarefa = ctk.CTkLabel(frame_tarefas, text=texto_formatado, font=("Arial", 14, "bold"))
            label_tarefa.configure(text_color="gray")
            label_tarefa.pack(pady=5, anchor="w")


def adicionar_tarefa(event=None):
    texto_tarefa = entrada_tarefa.get().title().strip()
    if texto_tarefa == "":
        return
    
    tarefa_dicionario = {
        "titulo": texto_tarefa,
        "concluido": False
    }
    
    lista.append(tarefa_dicionario) 
    entrada_tarefa.delete(0, "end") 
    atualizar_lista_tarefas()


def remover_tarefa():
    if lista == []:
        messagebox.showerror("Erro", "A lista está vazia.")
        return
    else:
        valor_digitado = entrada_tarefa.get().strip()
        try:
            numero = int(valor_digitado)
            indice_real = numero - 1
            lista.pop(indice_real)
            entrada_tarefa.delete(0, "end") 
            atualizar_lista_tarefas()
        except (ValueError, IndexError):
            messagebox.showerror("Erro", "Digite um número válido correspondente à tarefa.")
        
def concluir_tarefa():
    if lista == []:
        messagebox.showerror("Erro", "A lista está vazia.")
        return
    else:
        valor_digitado = entrada_tarefa.get().strip()
        try:
            numero = int(valor_digitado)
            indice_real = numero - 1
            lista[indice_real]["concluido"] = True
            entrada_tarefa.delete(0, "end")
            atualizar_lista_tarefas()
        except (ValueError, IndexError):
            messagebox.showerror("Erro", "Digite um número válido correspondente à tarefa.")






janela = ctk.CTk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x500")
janela.maxsize(width=400, height=600)
janela.resizable(width=False, height=False)

# Título
titulo = ctk.CTkLabel(janela, text="Minhas Tarefas", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# Entrada de Texto
entrada_tarefa = ctk.CTkEntry(janela, placeholder_text="Digite aqui...", width=250, font=("Arial", 14, "bold"))
entrada_tarefa.bind("<Return>", adicionar_tarefa)
entrada_tarefa.pack(pady=10)

# Botão 
btn = ctk.CTkButton(master=janela, text="Adicionar tarefa", command=adicionar_tarefa, font=("Arial", 14, "bold"), fg_color="green")
btn.pack(pady=10)
btn2 = ctk.CTkButton(master=janela, text="Remover tarefa", command=remover_tarefa, font=("Arial", 14, "bold"), fg_color="red")
btn2.pack(pady=10)
btn3 = ctk.CTkButton(master=janela, text="Concluir tarefa", command=concluir_tarefa, font=("Arial", 14, "bold"))
btn3.pack(pady=10)
# O Frame de Rolagem onde as tarefas vão aparecer
frame_tarefas = ctk.CTkScrollableFrame(janela, width=370, height=300)
frame_tarefas.pack(pady=10)


janela.mainloop()
