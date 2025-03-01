import tkinter as tk
import time

def atualizar_relogio():
    label.config(text=time.strftime("%H:%M:%S"))
    janela.after(1000, atualizar_relogio)

janela = tk.Tk()
janela.title("Relógio Digital")

label = tk.Label(janela, font=("Arial", 50), fg="white", bg="black")
label.pack()

atualizar_relogio()
janela.mainloop()
