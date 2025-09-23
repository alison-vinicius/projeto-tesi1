import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window("LOGIN")
app.geometry("500x500")
style = Style(theme="superhero")
style.colors.bg = "#5bc0de"       # fundo principal (claro)
style.colors.inputbg = "#ffffff"  # fundo dos campos Entry
style.colors.primary = "#5bc0de"  # azul claro para botões
style.colors.secondary = "#3498db"



label = ttk.Label(app, text="LOGIN")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill="x")
ttk.Label(email, text="Email:", font='Arial').pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=5)

senha = ttk.Frame(app)
senha.pack(pady=18, padx=10, fill="x")
ttk.Label(senha, text='Senha:', font='Arial').pack(side=LEFT, padx=5)
ttk.Entry(senha, show="*" ).pack(side=LEFT, fill="x", expand=True, padx=5)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, text="Enviar", bootstyle=SUCCESS).pack(side=LEFT, padx=15)
ttk.Button(botao, text="cancelar", bootstyle=DANGER).pack(side=LEFT, padx=15)


app.mainloop()