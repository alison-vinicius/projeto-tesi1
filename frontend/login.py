import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Login:
    def __init__(self, master):
        self.janela = master
    
        self.janela.title('LOGIN')
        self.janela.geometry('500x500')
        self.lbl_login = ttk.Label(self.janela, text='LOGIN')
        self.lbl_login.config(font=("Arial", 20, "bold"))
        self.lbl_login.pack(pady=35)

        self.email = ttk.Frame(self.janela)
        self.email.pack(pady=18, padx=10, fill="x")
        self.lbl_email = ttk.Label(self.email, text="Email:", font='Arial')
        self.lbl_email.pack(side=LEFT, padx=5)
        self.ent_email = ttk.Entry(self.email)
        self.ent_email.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.senha = ttk.Frame(self.janela)
        self.senha.pack(pady=18, padx=10, fill="x")
        self.lbl_senha = ttk.Label(self.senha, text='Senha:', font='Arial')
        self.lbl_senha.pack(side=LEFT, padx=5)
        self.ent_senha = ttk.Entry(self.senha, show="*" )
        self.ent_senha.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.botao = ttk.Frame(self.janela)
        self.botao.pack(pady=30, padx=10, fill="x")
        self.btn_cencelar_login = ttk.Button(self.botao, text="cancelar", bootstyle=DANGER)
        self.btn_cencelar_login.pack(side=LEFT, padx=100)
        self.btn_entrar_login = ttk.Button(self.botao, text="entrar", bootstyle=SUCCESS)
        self.btn_entrar_login.pack(side=LEFT, padx=15)


        

        

gui = ttk.Window(themename='superhero')
Login(gui)
gui.mainloop()