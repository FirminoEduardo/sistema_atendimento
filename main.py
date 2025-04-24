import _tkinter as tk
from gui.painel import PainelAtendimento

if __name__ == "__main__":
    root = tk.Tk()
    app = PainelAtendimento(root)
    root.mainloop()