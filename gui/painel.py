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

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.status_label.pack(pady=5)

        btn_comum = tk.Button(root, text="Retirar Senha Comum", font=("Arial", 14),
                              command=lambda: self.gerar_senha("comum"))
        btn_comum.pack(pady=5)

        btn_prioritaria = tk.Button(root, text="Retirar Senha Prioritária", font=("Arial", 14),
                                    command=lambda: self.gerar_senha("prioritaria"))
        btn_prioritaria.pack(pady=5)

        self.btn_chamar = tk.Button(root, text="Chamar Próxima", font=("Arial", 14),
                                    command=self.chamar_proxima)
        self.btn_chamar.pack(pady=10)

    def gerar_senha(self, tipo):
        senha = self.service.gerar_senha(tipo)
        messagebox.showinfo("Senha Gerada", f"Sua senha é: {senha}")

    def chamar_proxima(self):
        senha = self.service.chamar_proxima()
        if senha:
            self.label_senha.config(text=f"Senha Atual: {senha}")
            self.status_label.config(text=f"Atendendo {senha}...")
            self.btn_chamar.config(state="disabled")  # Desativa botão

            # Simula atendimento de 5 segundos (5000 milissegundos)
            self.root.after(5000, self.finalizar_atendimento)
        else:
            messagebox.showwarning("Fila Vazia", "Nenhuma senha na fila.")

    def finalizar_atendimento(self):
        self.status_label.config(text="Atendimento finalizado.")
        self.btn_chamar.config(state="normal")