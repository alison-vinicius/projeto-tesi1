import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_acompanhar_entrega import AcompanharEntregaController

class acompanharEntregaView(ttk.Toplevel):
    def __init__(self, master, email, senha):
        super().__init__(master)
        self.master = master
        self.email = email
        self.senha = senha
        self.title("STATUS DE ENTREGA")
        self.geometry("600x400")
        self.place_window_center()

        

        self.controller = AcompanharEntregaController()
        self.lbl_titulo = ttk.Label(self, text="SOLICITAÇÕES FEITAS", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12))  # Aumenta a fonte do texto nas células
        
        # 2. Configura a fonte dos cabeçalhos das colunas
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))

        # Estilo para as linhas com status 'pendente' (vermelho)
        style.configure("vermelho.Treeview", background="#bc1919", foreground="black") # Cor de fundo mais clara para melhor visualização
        
        # Cria o Treeview (Tabela)
        self.tabela = ttk.Treeview(self, columns=("Quantidade", "Data", "Status"), show="headings", height=10)
        self.tabela.pack(padx=20, pady=10, fill="both", expand=True)

        # Define os cabeçalhos das colunas
        self.tabela.heading("Quantidade", text="Quantidade", anchor="center")
        self.tabela.heading("Data", text="Data da Solicitação", anchor="center")
        self.tabela.heading("Status", text="Status", anchor="center")
        
        # Configura o alinhamento das colunas
        self.tabela.column("Quantidade", width=100, anchor="center")
        self.tabela.column("Data", width=150, anchor="center")
        self.tabela.column("Status", width=150, anchor="center")

        self.carregar_dados()
    

    def carregar_dados(self):
        """
        Busca os dados com a controller e insere no Treeview.
        """
        # Limpa a tabela antes de carregar novos dados
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        # Pega as solicitações da controller
        solicitacoes = self.controller.obter_solicitacoes(self.email, self.senha)
        
        if solicitacoes:
            for solicitacao in solicitacoes:
                # status = solicitacao[2]
            
                    
                self.tabela.insert("", "end", values=solicitacao)
        else:
            self.tabela.insert("", "end", values=("Nenhuma solicitação encontrada.", "", ""))
    
        