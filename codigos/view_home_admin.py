import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomeAdminView(ttk.Toplevel):
    def __init__(self, master):
        # Inicializa a Toplevel
        super().__init__(master)
        
        # Configura a própria janela (self)
        self.title('PÁGINA ADMIN')
        self.geometry("1000x1000")
        self.place_window_center()

        # Adiciona os widgets a 'self'
        self.lbl_titulo = ttk.Label(self, text='BEM VINDO ADMIN')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.botao = ttk.Frame(self) 
        self.botao.pack(pady=30, padx=10, fill="x")
        
        self.btn_cencelar_login = ttk.Button(self.botao, text="cancelar", bootstyle=DANGER)
        self.btn_cencelar_login.pack(side=LEFT, padx=100)
        
        self.btn_entrar_login = ttk.Button(self.botao, text="entrar", bootstyle=SUCCESS)
        self.btn_entrar_login.pack(side=LEFT, padx=15)

# Código para teste, se quiser rodar este arquivo separadamente
# if __name__ == '__main__':
#     # Cria uma janela raiz principal apenas para o teste
#     root = ttk.Window(themename='superhero')
#     root.withdraw() # Esconde a janela raiz
#     app = HomeAdminView(root)
#     root.mainloop()