import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class HomeSolicitanteView(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.janela = master
        self.janela.title('PANIEL SOLICITANTE')
        self.janela.geometry("1000x1000")
        self.place_window_center()
        self.lbl_titulo = ttk.Label(self, text='BEM VINDO SOLICITANTE')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.frame_botoes = ttk.Frame(self)
        self.frame_botoes.pack(expand=True, anchor="center")

        # -- botão solicitar troca de galão

        self.img_galao = self.carregar_imagem("trocaGalao.png", (350, 350))
        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="solicite um novo galão aqui",
            image=self.img_galao,
            compound="top",
            bootstyle="primary",
            command=self.solicitar_galao
        )
        self.btn_acompanhar.pack(side="left", padx=100)


        self.img_status_entrega = self.carregar_imagem("statusEntrega.png", (350, 350))
        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="Acompanhar status de entrega",
            image=self.img_status_entrega,
            compound="top",
            bootstyle="primary",
            # command=self.acompanhar_status
        )
        self.btn_acompanhar.pack(side="left", padx=100)
    
    def carregar_imagem(self, nome_arquivo, tamanho):
        caminho_imagem = f"imagens/{nome_arquivo}" # Altere para o caminho dos seus ícones
        img = Image.open(caminho_imagem)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    
    def solicitar_galao(self):
        print("oi")
        

        