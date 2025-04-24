class Senha:
    def __init__(self, codigo: str, tipo: str = "comum"):
        self.codigo = codigo
        self.tipo = tipo # "comum" ou "prioritaria"

    def __str__(self):
        return self.codigo
    
    def __str__(self):
        prefixo = "P" if self.tipo == "prioritaria" else "N"
        return f"{prefixo}{self.codigo}" 
    