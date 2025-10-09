import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

class HomeAdminView(ttk.Toplevel):
    def __init__(self, master):
     
        super().__init__(master)
        

        self.title('PÁGINA ADMIN')
        self.geometry("1000x1000")
        self.place_window_center()

        
        self.lbl_titulo = ttk.Label(self, text='BEM VINDO ADMIN')
        self.lbl_titulo.config(font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=35)

        self.botao = ttk.Frame(self) 
        self.botao.pack(pady=30, padx=10, fill="x")

        self.frame_botoes = ttk.Frame(self)
        self.frame_botoes.pack(expand=True, anchor="center")

        self.ger_funcionarios = self.carregar_imagem("gerenciarFuncionarios.png", (350, 350))
        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="gerenciar funcionários,",
            image=self.ger_funcionarios,
            compound="top",
            bootstyle="primary",
            # command=self.solicitar_galao
        )
        self.btn_acompanhar.pack(side="left", padx=100)


        self.vis_relatorios = self.carregar_imagem("visualizarRelatorios.png", (350, 350))
        self.btn_acompanhar = ttk.Button(
            self.frame_botoes, 
            text="visualizar reltórios",
            image=self.vis_relatorios,
            compound="top",
            bootstyle="primary",
            # command=self.solicitar_galao
        )
        self.btn_acompanhar.pack(side="left", padx=100)
    

    def carregar_imagem(self, nome_arquivo, tamanho):
        caminho_imagem = f"imagens/{nome_arquivo}" # Altere para o caminho dos seus ícones
        img = Image.open(caminho_imagem)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)





# Código para teste, se quiser rodar este arquivo separadamente
# if __name__ == '__main__':
#     # Cria uma janela raiz principal apenas para o teste
#     root = ttk.Window(themename='superhero')
#     root.withdraw() # Esconde a janela raiz
#     app = HomeAdminView(root)
#     root.mainloop()