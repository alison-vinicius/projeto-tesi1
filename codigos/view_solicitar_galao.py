import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from controller_solicitar_galao import SolicitarGalaoController


class SolicitarGalaoView(ttk.Toplevel):
    def __init__(self, master, email, senha):
        super().__init__(master)
        self.master = master
        self.email = email
        self.senha = senha
        self.title("Solicitar Troca de Galão")
        self.geometry("600x400")
        self.place_window_center()
        self.controller = SolicitarGalaoController(self.email, self.senha)

        self.lbl_titulo = ttk.Label(self, text= "SOLICITE UM NOVO GALÃO AQUI")
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.quantidade = ttk.Frame(self)
        self.quantidade.pack(pady=10, padx=20, fill="x")
        self.lbl_quantidade = ttk.Label(self.quantidade, text="quantidade:", font='Arial', width=12)
        self.lbl_quantidade.pack(side=LEFT, padx=5)
        self.ent_quantidade = ttk.Entry(self.quantidade)
        self.ent_quantidade.pack(side=LEFT, fill="x", expand=True, padx=5)

        self.observacao = ttk.Frame(self)
        self.observacao.pack(pady=10, padx=20, fill="x")
        self.lbl_observacao = ttk.Label(self.observacao, text="observacao:", font='Arial', width=12)
        self.lbl_observacao.pack(side=LEFT, padx=5)
        self.ent_observacao = ttk.Entry(self.observacao)
        self.ent_observacao.pack(side=LEFT, fill="x", expand=True, padx=5)

        


        self.botao = ttk.Frame(self)
        self.botao.pack(pady=20, padx=20, fill="x")

        self.btn_enviar_sol = ttk.Button(self.botao, text="Enviar", bootstyle=SUCCESS, command=self.enviar)
        self.btn_enviar_sol.pack(side=LEFT, expand=True, fill='x', padx=5)

        
    
    def enviar(self):
        quantidade_sol = self.ent_quantidade.get()
        obs = self.ent_observacao.get()
    
        sucesso = self.controller.solicitar(quantidade_sol, obs)
        
           
        


        
