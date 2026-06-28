import tkinter as tk


class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Catalogo de Prestadores de Serviço em Tecnologia da Informação (TI)")
        self.geometry("900x600")



        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width = 600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        titulo = tk.Label(self.titulo,
                        text="Cadastro",
                        font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        #LadoEsquerdo
        self.lado_esquerdo = tk.Frame(self, width = 300)
        self.lado_esquerdo.grid(row=1, column=0, sticky="nsew")

        self.lado_direito = tk.Frame(self, width = 300)
        self.lado_direito.grid(row=1, column=1, sticky="nsew", padx= 30)

        

        #Preencher os lados

        self.construir_esquerda()

        self.construir_direita()


    def construir_esquerda(self):
        #NOME
        nome = tk.Label(self.lado_esquerdo,
                        text="Nome",
                        font=("Arial", 14, "bold"))
        nome.pack(pady=10, padx=10)

        campo_nome = tk.Entry(self.lado_esquerdo)
        campo_nome.pack(padx=(20,20))

        #CPF
        cpf = tk.Label(self.lado_esquerdo,
                        text="CPF ou CNPJ",
                        font=("Arial", 14, "bold"))
        cpf.pack(pady=10, padx=10)

        campo_cpf = tk.Entry(self.lado_esquerdo)
        campo_cpf.pack(padx=(20,20))

        #NASCIMENTO
        nascimento = tk.Label(self.lado_esquerdo,
                        text="Data de Nascimento",
                        font=("Arial", 14, "bold"))
        nascimento.pack(pady=10, padx=10)

        #DATA
        campo_data = tk.Frame(self.lado_esquerdo)
        campo_data.pack(pady=5)
        dia = tk.Spinbox(campo_data, 
                         from_=1,    to=31,   
                         width=4, 
                         font=("Arial", 12))
        mes = tk.Spinbox(campo_data, 
                         from_=1,    to=12,   
                         width=4, 
                         font=("Arial", 12))
        ano = tk.Spinbox(campo_data, 
                         from_=1900, to=2026, 
                         width=6, 
                         font=("Arial", 12))

        dia.pack(side="left", padx=2)
        tk.Label(campo_data, text="/").pack(side="left")
        mes.pack(side="left", padx=2)
        tk.Label(campo_data, text="/").pack(side="left")
        ano.pack(side="left", padx=2)

        contato = tk.Label(self.lado_esquerdo,
                        text="Contato",
                        font=("Arial", 14, "bold"))
        contato.pack(pady=10, padx=10)

        campo_contato= tk.Entry(self.lado_esquerdo)
        campo_contato.pack(padx=(20,20))


    def construir_direita(self):
        cep = tk.Label(self.lado_direito,
                        text="CEP",
                        font=("Arial", 14, "bold"))
        cep.pack(pady=10, padx=10)

        campo_cep = tk.Entry(self.lado_direito)
        campo_cep.pack(padx=(20,20))



        


janela = Aplicativo()
janela.mainloop()