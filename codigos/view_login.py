import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_login import LoginController
from view_home_admin import HomeAdminView


class Login_view:
    def __init__(self, master):
        self.janela = master
        self.controller = LoginController()
        # Criação de um StringVar para o texto do resultado
        self.status_message = ttk.StringVar()
    
        self.janela.title('LOGIN')
        self.janela.geometry('1000x1000')
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

        # Label para a mensagem de status, usando textvariable
        self.lbl_status = ttk.Label(self.janela, textvariable=self.status_message, font=('Arial', 15))
        self.lbl_status.pack(pady=10)

        self.botao = ttk.Frame(self.janela)
        self.botao.pack(pady=30, padx=10, fill="x")
        self.btn_cencelar_login = ttk.Button(self.botao, text="cancelar", bootstyle=DANGER)
        self.btn_cencelar_login.pack(side=LEFT, padx=100)
        self.btn_entrar_login = ttk.Button(self.botao, text="entrar", bootstyle=SUCCESS, command=self.enviar_dados)
        self.btn_entrar_login.pack(side=LEFT, padx=15)

    def enviar_dados(self):
        email_digitado = self.ent_email.get()
        senha_digitada = self.ent_senha.get()

        # Chama a função da controller e recebe o resultado
        sucesso, mensagem, tipo_de_usuario = self.controller.fazer_login(email_digitado, senha_digitada)
    
        
        # Atualiza a mensagem na interface
        
        
        if sucesso:
            self.janela.destroy()
            nova_home = ttk.Window(themename='superhero')
            if tipo_de_usuario == "ADMIN":
                app_admin = HomeAdminView(nova_home)
            elif tipo_de_usuario == "FUNCIONARIO":
                print("funcionário")
            elif tipo_de_usuario == "SOLICITANTE":
                print("SOLICITANTE")

                
        else:
            self.status_message.set(mensagem)
            self.lbl_status.config(bootstyle=DANGER)

    
            


        

        

gui = ttk.Window(themename='superhero')
Login_view(gui)
gui.mainloop()