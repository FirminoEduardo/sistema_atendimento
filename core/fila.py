from collections import deque
from core.senha import Senha

class FilaSenhas:
    def __init__(self):
        self._fila_comum = deque()
        self._fila_prioritaria = deque()
        self._contador = 1

    def adicionar_senha(self, tipo: str = "comum") -> Senha:
        codigo = f"{self._contador:03d}"
        senha = Senha(codigo, tipo)
        if tipo == "prioritaria":
            self._fila_prioritaria.append(senha)
        else:
            self._fila_comum.append(senha)
        self._contador += 1
        return senha

    def proxima_senha(self) -> Senha | None:
        if self._fila_prioritaria:
            return self._fila_prioritaria.popleft()
        elif self._fila_comum:
            return self._fila_comum.popleft()
        return None