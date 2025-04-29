import tkinter as tk
from tkinter import messagebox
from services.atendimento_service import AtendimentoService
from gui.painel_chamadas import PainelChamadas
from utils.audio import tocar_som

class PainelAtendimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Atendimento Bancário")
        self.service = AtendimentoService()
        self.painel_chamadas = PainelChamadas()

        self.label_senha = tk.Label(root, text="Senha Atual: ---", font=("Arial", 24), fg="blue")
        self.label_senha.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.status_label.pack(pady=5)

        # Botões para retirada de senha
        btn_comum = tk.Button(root, text="Retirar Senha Comum", font=("Arial", 14),
                              command=lambda: self.gerar_senha("comum"))
        btn_comum.pack(pady=5)

        btn_prioritaria = tk.Button(root, text="Retirar Senha Prioritária", font=("Arial", 14),
                                    command=lambda: self.gerar_senha("prioritaria"))
        btn_prioritaria.pack(pady=5)

        # Guichês
        guiche_frame = tk.LabelFrame(root, text="Guichês", padx=10, pady=10)
        guiche_frame.pack(pady=15)

        self.guiche_botoes = []
        for i in range(1, 4):  # 3 guichês
            btn = tk.Button(guiche_frame, text=f"Guichê {i}", font=("Arial", 12),
                            command=lambda g=i: self.chamar_proxima(g))
            btn.grid(row=0, column=i-1, padx=10)
            self.guiche_botoes.append(btn)

    def gerar_senha(self, tipo):
        senha = self.service.gerar_senha(tipo)
        messagebox.showinfo("Senha Gerada", f"Sua senha é: {senha}")

    def chamar_proxima(self, guiche):
        senha = self.service.chamar_proxima()
        if senha:
            self.label_senha.config(text=f"Senha Atual: {senha}")
            self.status_label.config(text=f"Atendendo {senha} no Guichê {guiche}")
            self.painel_chamadas.atualizar_senha(f"{senha} - Guichê {guiche}")
            tocar_som("assets/ding.mp3")

            for btn in self.guiche_botoes:
                btn.config(state="disabled")

            self.root.after(5000, self.finalizar_atendimento)
        else:
            messagebox.showwarning("Fila Vazia", "Nenhuma senha na fila.")

    def finalizar_atendimento(self):
        self.status_label.config(text="Atendimento finalizado.")
        for btn in self.guiche_botoes:
            btn.config(state="normal")