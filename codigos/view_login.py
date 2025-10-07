import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_login import LoginController
from view_home_admin import HomeAdminView
from view_home_funcionario import HomeFuncionarioView
from view_home_solicitante import HomeSolicitanteView


class Login_view:
    def __init__(self, master):
        self.janela = master
        self.controller = LoginController()
        self.status_message = ttk.StringVar()
    
        self.janela.title('LOGIN')
        self.janela.geometry('500x400') # Ajustei o tamanho para ficar mais proporcional
        self.janela.place_window_center() # Centraliza a janela

        self.lbl_login = ttk.Label(self.janela, text='LOGIN', font=("Arial", 20, "bold"))
        self.lbl_login.pack(pady=20)

        self.email = ttk.Frame(self.janela)
        self.email.pack(pady=10, padx=20, fill="x")
        self.lbl_email = ttk.Label(self.email, text="Email:", font='Arial', width=6)
        self.lbl_email.pack(side=LEFT, padx=5)
        self.ent_email = ttk.Entry(self.email)
        self.ent_email.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.senha = ttk.Frame(self.janela)
        self.senha.pack(pady=10, padx=20, fill="x")
        self.lbl_senha = ttk.Label(self.senha, text='Senha:', font='Arial', width=6)
        self.lbl_senha.pack(side=LEFT, padx=5)
        self.ent_senha = ttk.Entry(self.senha, show="*")
        self.ent_senha.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.lbl_status = ttk.Label(self.janela, textvariable=self.status_message, font=('Arial', 12))
        self.lbl_status.pack(pady=10)

        self.botao = ttk.Frame(self.janela)
        self.botao.pack(pady=20, padx=20, fill="x")
        
        # Adicionei expand=True e fill='x' para os botões ocuparem o espaço
        self.btn_cencelar_login = ttk.Button(self.botao, text="Cancelar", bootstyle=DANGER)
        self.btn_cencelar_login.pack(side=LEFT, expand=True, fill='x', padx=5)
        
        self.btn_entrar_login = ttk.Button(self.botao, text="Entrar", bootstyle=SUCCESS, command=self.enviar_dados)
        self.btn_entrar_login.pack(side=LEFT, expand=True, fill='x', padx=5)

    def enviar_dados(self):
        email_digitado = self.ent_email.get()
        senha_digitada = self.ent_senha.get()

        # Chama a função da controller e recebe o resultado
        sucesso, mensagem, tipo_de_usuario = self.controller.fazer_login(email_digitado, senha_digitada)
    
        
        # Atualiza a mensagem na interface
        # nova_home = ttk.Window(themename='superhero')
        if sucesso:
            self.janela.withdraw()
            if tipo_de_usuario == "ADMIN":
                app_admin = HomeAdminView(self.janela)
            elif tipo_de_usuario == "FUNCIONARIO":
                app_funcionario = HomeFuncionarioView(self.janela)
            elif tipo_de_usuario == "SOLICITANTE":
                app_solicitante = HomeSolicitanteView(self.janela)

                
        else:
            self.status_message.set(mensagem)
            self.lbl_status.config(bootstyle=DANGER)

    
            


        

        
if __name__ == "__main__":
    gui = ttk.Window(themename='superhero')
    Login_view(gui)
    gui.mainloop()