import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from controller_acompanhar_entrega import AcompanharEntregaController

class GerenciarFuncionariosView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("GERENCIAR FUNCIONÁRIOS")
        self.geometry("600x400")
        self.place_window_center()

        # self.controller = AcompanharEntregaController()
        self.lbl_titulo = ttk.Label(self, text="GERENCIAR FUNCIONÁRIOS", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)
