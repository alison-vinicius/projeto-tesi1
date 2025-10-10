import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_mudar_status import MudarStatusController
class MudarStatusView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("GERENCIAR SOLICITAÇÕES")
        self.geometry("900x600")
        self.place_window_center()
        
        self.controller = MudarStatusController()


        self.lbl_titulo = ttk.Label(self, text="GERENCIAR SOLICITAÇÕES", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        # --- Configuração dos Estilos para Cores ---
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
        style.configure("pendente.Treeview", background="#ffcccc", foreground="black") # Vermelho claro
        style.configure("concluido.Treeview", background="#ccffcc", foreground="black") # Verde claro
        style.configure("andamento.Treeview", background="#cce0ff", foreground="black") # Azul claro
        style.configure("interrompido.Treeview", background="#ffffcc", foreground="black") # Amarelo claro
        
        # Cria o Treeview
        self.tabela = ttk.Treeview(self, columns=("ID", "Quantidade", "Data", "Status", "Observação"), show="headings", height=10)
        self.tabela.pack(padx=20, pady=10, fill="both", expand=True)

        # Configura as colunas
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Quantidade", text="Quantidade")
        self.tabela.heading("Data", text="Data da Solicitação")
        self.tabela.heading("Status", text="Status")
        self.tabela.heading("Observação", text="Observação")

        # Esconde a coluna ID e ajusta a largura das outras
        self.tabela.column("ID", width=0, stretch=False) 
        self.tabela.column("Quantidade", width=80, anchor="center")
        self.tabela.column("Data", width=160, anchor="center")
        self.tabela.column("Status", width=100, anchor="center")
        self.tabela.column("Observação", width=400, anchor="w")

        # Adiciona um frame para os controles de edição
        self.frm_controles = ttk.Frame(self)
        self.frm_controles.pack(pady=20)
        
        ttk.Label(self.frm_controles, text="Atualizar Status:").pack(side="left", padx=10)
        
        # Cria o Combobox com as opções de status
        self.cmb_status = ttk.Combobox(self.frm_controles, values=["em andamento", "concluído", "interrompido"], state="readonly")
        self.cmb_status.pack(side="left", padx=10)
        
        # Botão para atualizar
        self.btn_atualizar = ttk.Button(self.frm_controles, text="Atualizar", command=self.atualizar_status, bootstyle="info")
        self.btn_atualizar.pack(side="left", padx=10)
        
        # Label de status para feedback
        self.lbl_status = ttk.Label(self, text="", font=("Arial", 12))
        self.lbl_status.pack(pady=5)

        self.carregar_dados()
        self.tabela.bind("<<TreeviewSelect>>", self.on_item_select)

    def carregar_dados(self):
        """
        Busca todos os dados com a controller e insere no Treeview.
        """
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        solicitacoes = self.controller.obter_todas_solicitacoes()
        
        if solicitacoes:
            for solicitacao in solicitacoes:
                # O status é o 4º item (índice 3) na tupla
                status = solicitacao[3] 
                
                # Mapeia o status para a tag de cor
                if status == "pendente":
                    tag = "pendente"
                elif status == "concluído":
                    tag = "concluido"
                elif status == "em andamento":
                    tag = "andamento"
                elif status == "interrompido":
                    tag = "interrompido"
                else:
                    tag = ""
                
                # Insere a linha na tabela com o ID e a tag de cor
                self.tabela.insert("", "end", values=solicitacao, tags=(tag,))
        else:
            self.tabela.insert("", "end", values=("Nenhuma solicitação encontrada.", "", "", "", ""))
    
    def on_item_select(self, event):
        """
        Armazena o ID da solicitação selecionada.
        """
        # Limpa o label de status anterior
        self.lbl_status.config(text="")
        
        # Pega o ID do item selecionado
        item_id = self.tabela.selection()[0]
        # Pega os valores da linha (a primeira coluna é o ID que queremos)
        self.item_selecionado = self.tabela.item(item_id, 'values')[0]
        
        # Pega o status atual e preenche o Combobox
        status_atual = self.tabela.item(item_id, 'values')[3]
        self.cmb_status.set(status_atual)
        
    def atualizar_status(self):
        """
        Chama o controller para atualizar o status da solicitação selecionada.
        """
        if not self.item_selecionado:
            self.lbl_status.config(text="Selecione uma solicitação para atualizar.", bootstyle="danger")
            return
            
        novo_status = self.cmb_status.get()
        if not novo_status:
            self.lbl_status.config(text="Selecione um novo status.", bootstyle="danger")
            return
            
        sucesso = self.controller.atualizar_status(self.item_selecionado, novo_status)
        
        if sucesso:
            self.lbl_status.config(text="Status atualizado com sucesso!", bootstyle="success")
            # Recarrega a tabela para mostrar o status atualizado
            self.carregar_dados()
            # Limpa a seleção
            self.tabela.selection_set("")
            self.item_selecionado = None
        else:
            self.lbl_status.config(text="Erro ao atualizar o status.", bootstyle="danger")