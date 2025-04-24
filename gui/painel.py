import tkinter as tk
from tkinter import messagebox
from services.atendimento_service import AtendimentoService

class PainelAtendimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Atendimento Bancário")
        self.service = AtendimentoService

        # Exibição da senha atual
        self.label_senha = tk.Label(root, text="Senha Atual: ---", font=("Arial", 24), fg="blue")
        self.label_senha.pack(pady=20)

        # Botões
        btn_gerar = tk.Button(root, text="Retirar Senha", font=("Arial", 14), command=self.gerar_senha)
        btn_gerar.pack(pady=10)

        btn_chamar = tk.Button(root, text="Chamar Próxima", font=("Arial", 14), command=self.chamar_proxima)
        btn_chamar.pack(pady=10)

      def gerar_senha(self):
        senha = self.service.gerar_senha()
        messagebox.showinfo("Senha Gerada", f"Sua senha é: {senha}")

    def chamar_proxima(self):
        senha = self.service.chamar_proxima()
        if senha:
            self.label_senha.config(text=f"Senha Atual: {senha}")
        else:
            messagebox.showwarning("Fila Vazia", "Nenhuma senha na fila.")