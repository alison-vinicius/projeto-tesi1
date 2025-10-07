import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomeFuncionarioView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.janela = master
        self.janela.title('PÁGINA FUNCIONARIO')
        self.janela.geometry("1000x1000")
        self.place_window_center()

        self.lbl_titulo = ttk.Label(self, text='BEM VINDO FUNCIONARIO')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)
    