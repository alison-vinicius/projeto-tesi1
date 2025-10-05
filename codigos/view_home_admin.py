import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomeAdminView(ttk.Toplevel):
    def __init__(self, master):
        self.janela = master
        self.janela.title('PÁGINA ADMIN')
        self.janela.geometry("1000x1000")
        self.lbl_titulo = ttk.Label(self.janela, text='BEM VINDO ADMIN')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)
    




# gui = ttk.Window(themename='superhero')
# HomeAdminView(gui)
# gui.mainloop()