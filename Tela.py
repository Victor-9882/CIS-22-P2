import tkinter as tk


class TelaCadastro(tk.Tk):
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

        #Botão Inferior
        self.contruir_botao()






    def construir_esquerda(self):
        #NOME
        nome = tk.Label(self.lado_esquerdo,
                        text="Nome",
                        font=("Arial", 14, "bold"))
        nome.pack(pady=10, padx=10)

        self.campo_nome = tk.Entry(self.lado_esquerdo)
        self.campo_nome.pack(padx=(20,20))

        #CPF
        cpf = tk.Label(self.lado_esquerdo,
                        text="CPF ou CNPJ",
                        font=("Arial", 14, "bold"))
        cpf.pack(pady=10, padx=10)

        self.campo_cpf = tk.Entry(self.lado_esquerdo)
        self.campo_cpf.pack(padx=(20,20))

        #NASCIMENTO
        nascimento = tk.Label(self.lado_esquerdo,
                        text="Data de Nascimento",
                        font=("Arial", 14, "bold"))
        nascimento.pack(pady=10, padx=10)

        #DATA
        campo_data = tk.Frame(self.lado_esquerdo)
        campo_data.pack(pady=5)
        self.dia = tk.Spinbox(campo_data, 
                         from_=1,    to=31,   
                         width=4, 
                         font=("Arial", 12))
        self.mes = tk.Spinbox(campo_data, 
                         from_=1,    to=12,   
                         width=4, 
                         font=("Arial", 12))
        self.ano = tk.Spinbox(campo_data, 
                         from_=1900, to=2026, 
                         width=6, 
                         font=("Arial", 12))

        self.dia.pack(side="left", padx=2)
        tk.Label(campo_data, text="/").pack(side="left")
        self.mes.pack(side="left", padx=2)
        tk.Label(campo_data, text="/").pack(side="left")
        self.ano.pack(side="left", padx=2)

        contato = tk.Label(self.lado_esquerdo,
                        text="Contato",
                        font=("Arial", 14, "bold"))
        contato.pack(pady=10, padx=10)

        self.campo_contato= tk.Entry(self.lado_esquerdo)
        self.campo_contato.pack(padx=(20,20))


    def construir_direita(self):
        self.lado_direito.grid_columnconfigure(0, weight=1)
        self.lado_direito.grid_columnconfigure(1, weight=1)
        self.lado_direito.grid_rowconfigure(1, weight=1)

        frame_cep = tk.Frame(self.lado_direito, width=300)
        frame_cep.grid(row = 0, column=0,columnspan=2, sticky="nsew")

        cep = tk.Label(frame_cep,
                        text="CEP",
                        font=("Arial", 14, "bold"))
        cep.pack(pady=10, padx=10)

        self.campo_cep = tk.Entry(frame_cep)
        self.campo_cep.pack(padx=(20,20))

        #Subdivisão


        frame_esquerda = tk.Frame(self.lado_direito, width = 150)
        frame_esquerda.grid(row=1, column=0, sticky="nsew")

        frame_direita = tk.Frame(self.lado_direito, width = 150)
        frame_direita.grid(row=1, column=1, sticky="nsew")

        #Esquerda

        rua = tk.Label(frame_esquerda,
                        text="Rua",
                        font=("Arial", 14, "bold"))
        rua.pack(pady=10, padx=10)

        self.campo_rua= tk.Entry(frame_esquerda)
        self.campo_rua.pack(padx=(20,20))

        numero = tk.Label(frame_esquerda,
                        text="Numero",
                        font=("Arial", 14, "bold"))
        numero.pack(pady=10, padx=10)

        self.campo_numero= tk.Entry(frame_esquerda)
        self.campo_numero.pack(padx=(20,20))

        cidade = tk.Label(frame_esquerda,
                        text="Cidade",
                        font=("Arial", 14, "bold"))
        cidade.pack(pady=10, padx=10)

        self.campo_cidade= tk.Entry(frame_esquerda)
        self.campo_cidade.pack(padx=(20,20))

        #Direita

        complemento = tk.Label(frame_direita,
                        text="Complemento",
                        font=("Arial", 14, "bold"))
        complemento.pack(pady=10, padx=10)

        self.campo_complemento= tk.Entry(frame_direita)
        self.campo_complemento.pack(padx=(20,20))

        bairro = tk.Label(frame_direita,
                        text="Bairro",
                        font=("Arial", 14, "bold"))
        bairro.pack(pady=10, padx=10)

        self.campo_bairro= tk.Entry(frame_direita)
        self.campo_bairro.pack(padx=(20,20))

        uf = tk.Label(frame_direita,
                        text="UF",
                        font=("Arial", 14, "bold"))
        uf.pack(pady=10, padx=10)

        self.campo_uf= tk.Entry(frame_direita)
        self.campo_uf.pack(padx=(20,20))

    def adicionar_usuario(self):

        data_nascimento = self.dia.get() + "-" + self.mes.get() + "-" + self.ano.get()
        #print(data_nascimento)
        return (
        self.campo_nome.get(),
        self.campo_cpf.get(),
        self.campo_cpf.get(),
        data_nascimento,
        self.campo_rua.get(),
        self.campo_numero.get(),
        self.campo_complemento.get(),
        self.campo_bairro.get(),
        self.campo_uf.get(),
        self.campo_cep.get(),
        self.campo_contato.get())

    def contruir_botao(self):
        frame_botao_adicionar = tk.Frame(self, width=600)
        frame_botao_adicionar.grid(row=2, column=0, sticky="ew")

        self.botao_adicionar = tk.Button(frame_botao_adicionar, 
                                         text="Adicionar Usuário",
                                         command=self.adicionar_usuario)
        self.botao_adicionar.pack(pady = 10)

        frame_botao_ver_users= tk.Frame(self, width=600)
        frame_botao_ver_users.grid(row=2, column=1, sticky="ew")

        self.botao_ver_users = tk.Button(frame_botao_ver_users, 
                                         text="Ver usuários")
        self.botao_ver_users.pack(pady = 10)



        


janela = TelaCadastro()
janela.mainloop()