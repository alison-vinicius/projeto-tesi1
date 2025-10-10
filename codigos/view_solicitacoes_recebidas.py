import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_solicitacoes_recebidas import SolicitantesRecebidasController

class SolicitacoesRecebidasView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("SOLCITAÇÕES RECEBIDAS")
        self.geometry("800x500")
        self.place_window_center()
        self.controller = SolicitantesRecebidasController()

    
        self.lbl_titulo = ttk.Label(self, text="SOLICITAÇÕES RECEBIDAS", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        # Cria o Treeview (Tabela)
        self.tabela = ttk.Treeview(self, columns=("Quantidade", "Data", "Status", "Observação"), show="headings", height=10)
        self.tabela.pack(padx=20, pady=10, fill="both", expand=True)

        # Define os cabeçalhos das colunas
        self.tabela.heading("Quantidade", text="Quantidade", anchor="center")
        self.tabela.heading("Data", text="Data da Solicitação", anchor="center")
        self.tabela.heading("Status", text="Status", anchor="center")
        self.tabela.heading("Observação", text="Observação", anchor="center")
        
        # Configura o alinhamento e largura das colunas
        self.tabela.column("Quantidade", width=100, anchor="center")
        self.tabela.column("Data", width=150, anchor="center")
        self.tabela.column("Status", width=100, anchor="center")
        self.tabela.column("Observação", width=250, anchor="w") # Alinhado à esquerda para o texto

        self.carregar_dados()
    
    def carregar_dados(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        
        solicitacoes = self.controller.obter_solicitacoes_pendentes()
        
        if solicitacoes:
            for solicitacao in solicitacoes:
                # Insere a linha na tabela com a tag 'vermelho' para pendente
                self.tabela.insert("", "end", values=solicitacao, tags=("vermelho",))
        else:
            self.tabela.insert("", "end", values=("Nenhuma solicitação pendente encontrada.", "", "", ""))