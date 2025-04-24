from core.fila import FilaSenhas
from core.senha import Senha

class AtendimentoService:
    def __init__(self):
        self.fila = FilaSenhas()
        self.senha_atual: Senha | None = None

    def gerar_senha(self, tipo: str = "comum") -> Senha:
        return self.fila.adicionar_senha(tipo)
    
    def chamar_proxima(self) -> Senha | None:
        self.senha_atual = self.fila.proxima_senha()
        return self.senha_atual