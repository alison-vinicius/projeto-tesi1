import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from view_solicitacoes_recebidas import SolicitacoesRecebidasView
from view_mudar_status import MudarStatusView

class HomeFuncionarioView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.janela = master
        self.janela.title('PÁGINA FUNCIONARIO')
        self.janela.geometry("1000x1000")
        self.place_window_center()

        self.lbl_titulo = ttk.Label(self, text='BEM VINDO FUNCIONARIO')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.frame_botoes = ttk.Frame(self)
        self.frame_botoes.pack(expand=True, anchor="center")


        self.img_visualizarSolicitacoes = self.carregar_imagem("visualizarSolicitacoes.png", (350, 350))

        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="visualizar novas solicitações",
            image=self.img_visualizarSolicitacoes,
            compound="top",
            bootstyle="primary",
            command=self.visualizar_sol
        )
        self.btn_acompanhar.pack(side="left", padx=100)


        self.mudar_status = self.carregar_imagem("mudarStatus.png", (350, 350))
        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="mudar status de entrega",
            image=self.mudar_status,
            compound="top",
            bootstyle="primary",
            command=self.acompanhar_status
        )
        self.btn_acompanhar.pack(side="left", padx=100)

    def carregar_imagem(self, nome_arquivo, tamanho):
        caminho_imagem = f"imagens/{nome_arquivo}" # Altere para o caminho dos seus ícones
        img = Image.open(caminho_imagem)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def visualizar_sol(self):
        vis_solicitacoes = SolicitacoesRecebidasView(self.janela)
        vis_solicitacoes.grab_set()
        vis_solicitacoes.wait_window()

    def acompanhar_status(self):
        vis_solicitacoes = MudarStatusView(self.janela)
        vis_solicitacoes.grab_set()
        vis_solicitacoes.wait_window()