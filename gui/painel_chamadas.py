import tkinter as tk

class PainelChamadas:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Painel de Chamadas")
        self.window.geometry("400x200")
        self.window.configure(bg="black")

        self.label = tk.Label(self.window, text="Aguardando...", font=("Arial", 48),
                              bg="black", fg="white")
        self.label.pack(expand=True)

    def atualizar_senha(self, senha):
        self.label.config(text=str(senha))