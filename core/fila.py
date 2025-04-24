from collections import deque
from core.senha import Senha

class FilaSenhas:
    def __init__(self):
        self.fila = deque()
        self._contador = 1

    def adicionar_senha(self) -> Senha:
        codigo = f"N{self._contador:03d}"
        senha = Senha(codigo)
        self._fila.append(senha)
        self._contador += 1
        return senha
    
    def proxima_senha(self) -> Senha | None:
        if self.fila:
            return self._fila.popleft()
        return None