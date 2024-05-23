import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        cm = float(entry_cm.get())
        metros = cm / 100
        label_resultado.config(text=f"{cm} centímetros é igual a: {metros:.2f} metros",font= 'arial' , fg= cor1, bg= cor2)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira um número válido.", font= 'arial', fg= cor1, bg= cor2)

janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")
janela.geometry("400x300")
cor1 = '#e2e2e2'
cor2 = '#797772'

label_cm = tk.Label(janela, text="Qual a medida em centímetros? ", font= 'arial', fg= cor1, bg= cor2 )
label_cm.grid(row=0, column=0, padx=10, pady=10)

entry_cm = tk.Entry(janela)
entry_cm.grid(row=0, column=1, padx=10, pady=10)

botao_converter = tk.Button(janela, text="Converter", command=converter, font= 'arial', fg= cor1, bg= cor2)
botao_converter.grid(row=1, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()
