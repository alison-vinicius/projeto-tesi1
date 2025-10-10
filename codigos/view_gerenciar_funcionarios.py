import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller_gerenciar_funcionario import GerenciarFuncionariosController
from ttkbootstrap.dialogs import Messagebox

class GerenciarFuncionariosView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("GERENCIAR FUNCIONÁRIOS")
        self.geometry("600x400")
        self.place_window_center()

        self.controller = GerenciarFuncionariosController()
        self.lbl_titulo = ttk.Label(self, text="GERENCIAR FUNCIONÁRIOS", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        # --- Treeview para a Lista de Funcionários ---
        self.tabela = ttk.Treeview(self, columns=("ID", "Nome", "Email", "Setor"), show="headings", height=10)
        self.tabela.pack(padx=20, pady=10, fill="both", expand=True)

        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Email", text="Email")
        self.tabela.heading("Setor", text="Setor")

        self.tabela.column("ID", width=0, stretch=False)
        self.tabela.column("Nome", width=200, anchor="w")
        self.tabela.column("Email", width=250, anchor="w")
        self.tabela.column("Setor", width=150, anchor="center")

        self.carregar_dados()

        # --- Frame para o Formulário e Botões ---
        self.frm_controles = ttk.Frame(self)
        self.frm_controles.pack(pady=20)

        # Campos de entrada
        self.lbl_nome = ttk.Label(self.frm_controles, text="Nome:")
        self.lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_nome = ttk.Entry(self.frm_controles)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_email = ttk.Label(self.frm_controles, text="Email:")
        self.lbl_email.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ent_email = ttk.Entry(self.frm_controles)
        self.ent_email.grid(row=1, column=1, padx=5, pady=5)
        
        self.lbl_senha = ttk.Label(self.frm_controles, text="Senha:")
        self.lbl_senha.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ent_senha = ttk.Entry(self.frm_controles, show="*")
        self.ent_senha.grid(row=2, column=1, padx=5, pady=5)
        
        # Botões de Ação
        self.btn_adicionar = ttk.Button(self.frm_controles, text="Adicionar", command=self.adicionar_funcionario, bootstyle="success")
        self.btn_adicionar.grid(row=3, column=0, padx=5, pady=10)
        
        self.btn_excluir = ttk.Button(self.frm_controles, text="Excluir", command=self.remover_funcionario, bootstyle="danger")
        self.btn_excluir.grid(row=3, column=1, padx=5, pady=10)

    def carregar_dados(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        funcionarios = self.controller.obter_todos_funcionarios()
        
        if funcionarios:
            for func in funcionarios:
                # Mostra apenas Nome, Email e Setor, mas armazena o ID
                self.tabela.insert("", "end", values=(func[0], func[1], func[2], func[5]))
        else:
            self.tabela.insert("", "end", values=("Nenhum funcionário encontrado.", "", "", ""))

    def adicionar_funcionario(self):
        """Adiciona um novo funcionário a partir dos campos do formulário."""
        nome = self.ent_nome.get()
        email = self.ent_email.get()
        senha = self.ent_senha.get()
        
        if not all([nome, email, senha]):
            Messagebox.show_warning(title="Atenção", message="Todos os campos devem ser preenchidos.")
            return

        sucesso = self.controller.adicionar_novo_funcionario(nome, email, senha)
        
        if sucesso:
            Messagebox.show_info(title="Sucesso", message="Funcionário adicionado com sucesso!")
            self.limpar_campos()
            self.carregar_dados() # Recarrega a tabela para mostrar o novo funcionário
        else:
            Messagebox.show_warning(title="Erro", message="Ocorreu um erro ao adicionar o funcionário.")
            
    def remover_funcionario(self):
        """Remove o funcionário selecionado na tabela."""
        item_selecionado = self.tabela.selection()
        if not item_selecionado:
            Messagebox.show_warning(title="Atenção", message="Selecione um funcionário para excluir.")
            return
        confirmar = Messagebox.show_question(title="Confirmar Exclusão", message="Tem certeza que deseja excluir o funcionário selecionado?")
        if confirmar == "Yes":
            id_usuario = self.tabela.item(item_selecionado, 'values')[0]
            sucesso = self.controller.remover_funcionario_existente(id_usuario)

            if sucesso:
                Messagebox.show_info(title="Sucesso", message="Funcionário excluído com sucesso!")
                self.carregar_dados() # Recarrega a tabela
            else:
                Messagebox.show_warning(title="Erro", message="Ocorreu um erro ao excluir o funcionário.")
    def limpar_campos(self):
        """Limpa todos os campos de entrada."""
        self.ent_nome.delete(0, "end")
        self.ent_email.delete(0, "end")
        self.ent_senha.delete(0, "end")
