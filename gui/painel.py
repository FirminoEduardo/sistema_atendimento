import tkinter as tk
from tkinter import messagebox
from services.atendimento_service import AtendimentoService

class PainelAtendimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Atendimento Bancário")
        self.service = AtendimentoService()

        self.label_senha = tk.Label(root, text="Senha Atual: ---", font=("Arial", 24), fg="blue")
        self.label_senha.pack(pady=20)

        btn_comum = tk.Button(root, text="Retirar Senha Comum", font=("Arial", 14),
                              command=lambda: self.gerar_senha("comum"))
        btn_comum.pack(pady=5)

        btn_prioritaria = tk.Button(root, text="Retirar Senha Prioritária", font=("Arial", 14),
                                    command=lambda: self.gerar_senha("prioritaria"))
        btn_prioritaria.pack(pady=5)

        btn_chamar = tk.Button(root, text="Chamar Próxima", font=("Arial", 14), command=self.chamar_proxima)
        btn_chamar.pack(pady=10)

    def gerar_senha(self, tipo):
        senha = self.service.gerar_senha(tipo)
        messagebox.showinfo("Senha Gerada", f"Sua senha é: {senha}")

    def chamar_proxima(self):
        senha = self.service.chamar_proxima()
        if senha:
            self.label_senha.config(text=f"Senha Atual: {senha}")
        else:
            messagebox.showwarning("Fila Vazia", "Nenhuma senha na fila.")