import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_cadastrar_solicitante import CadastrarSolicitanteController
class CadastrarSolicitanteView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("CADASTRE-SE")
        self.geometry("600x400")
        self.place_window_center()

        # self.controller = CadastrarSolicitanteController()
        self.lbl_titulo = ttk.Label(self, text="CADASTRE-SE", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.nome = ttk.Frame(self)
        self.nome.pack(pady=10, padx=20, fill="x")
        self.lbl_nome = ttk.Label(self.nome, text="nome:", font='Arial', width=6)
        self.lbl_nome.pack(side=LEFT, padx=5)
        self.ent_nome = ttk.Entry(self.nome)
        self.ent_nome.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.email = ttk.Frame(self)
        self.email.pack(pady=10, padx=20, fill="x")
        self.lbl_email = ttk.Label(self.email, text='email:', font='Arial', width=6)
        self.lbl_email.pack(side=LEFT, padx=5)
        self.ent_email = ttk.Entry(self.email)
        self.ent_email.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.senha = ttk.Frame(self)
        self.senha.pack(pady=10, padx=20, fill="x")
        self.lbl_senha = ttk.Label(self.senha, text='Senha:', font='Arial', width=6)
        self.lbl_senha.pack(side=LEFT, padx=5)
        self.ent_senha = ttk.Entry(self.senha, show="*")
        self.ent_senha.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.setor = ttk.Frame(self)
        self.setor.pack(pady=10, padx=20, fill="x")
        self.lbl_setor = ttk.Label(self.setor, text='Setor:', font='Arial', width=6)
        self.lbl_setor.pack(side=LEFT, padx=5)
        self.ent_setor = ttk.Entry(self.setor)
        self.ent_setor.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.botaoCad = ttk.Frame(self)
        self.botaoCad.pack(pady=20, padx=20, fill="x")
        self.btn_cadastrar = ttk.Button(self.botaoCad, text="Cadastrar", bootstyle=PRIMARY)
        self.btn_cadastrar.pack(side=LEFT, expand=True, fill='x', padx=5)

    # def enviar_dados_cadastrais(self):
    #     nome = self.ent_nome.get()
    #     email = self.ent_email.get()
    #     senha = self.ent_senha.get()
    #     setor = self.ent_setor.get()
    #     self.controller.dadosCadastrais(nome, email, senha, setor)
