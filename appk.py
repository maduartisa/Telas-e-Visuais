
import tkinter as tk

def clicar():
    label.config(text="Você clicou!")

janela = tk.Tk()

janela.title("Meu App")
janela.geometry("300x200")  # largura x altura
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()

label = tk.Label(janela, text="Clique no botão")
label.pack()

botao = tk.Button(janela, text="Clicar", command=clicar)
botao.pack()

janela.mainloop()

