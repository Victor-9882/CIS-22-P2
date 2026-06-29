import tkinter as tk
from Banco import Banco
from Check import CheckValidCPF, CheckValidCNPJ, AdressInformation


class App(tk.Tk):
    def __init__(self, Banco):
        super().__init__()
        self.geometry("900x600")

        self.banco = Banco
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TelaCadastro, TelaInicial, TelaSecundaria, TelaErroDocumento, TelaUsuarios, TelaSucesso, TelaErroCEP,
                  TelaDeletado):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(TelaCadastro)

    def mostrar_tela(self, classe):
        self.frames[classe].tkraise()


class TelaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Tela Inicial").pack(pady=20)
        tk.Button(self, text="Ir para Tela 2",
                  command=self.trocar_tela_secundaria).pack()

    def trocar_tela_secundaria(self):
        self.controller.mostrar_tela(TelaSecundaria)


class TelaSecundaria(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Tela Secundária").pack(pady=20)
        tk.Button(self, text="Voltar",
                  command=lambda: controller.mostrar_tela(TelaInicial)).pack()


class TelaUsuarios(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Divisão na Tela
        for i in range(13):
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=13, sticky="ew")

        titulo = tk.Label(self.titulo,
                          text="Lista de Usuários",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        # Colunas
        self.index = tk.Frame(self)
        self.index.grid(row=1, column=0, sticky="nsew")
        self.index_dados = tk.Frame(self.index)
        self.index_dados.pack(fill="both", expand=True)

        self.nome = tk.Frame(self)
        self.nome.grid(row=1, column=1, sticky="nsew")
        self.nome_dados = tk.Frame(self.nome)
        self.nome_dados.pack(fill="both", expand=True)

        self.cpf = tk.Frame(self)
        self.cpf.grid(row=1, column=2, sticky="nsew")
        self.cpf_dados = tk.Frame(self.cpf)
        self.cpf_dados.pack(fill="both", expand=True)

        self.cnpj = tk.Frame(self)
        self.cnpj.grid(row=1, column=3, sticky="nsew")
        self.cnpj_dados = tk.Frame(self.cnpj)
        self.cnpj_dados.pack(fill="both", expand=True)

        self.data = tk.Frame(self)
        self.data.grid(row=1, column=4, sticky="nsew")
        self.data_dados = tk.Frame(self.data)
        self.data_dados.pack(fill="both", expand=True)

        self.rua = tk.Frame(self)
        self.rua.grid(row=1, column=5, sticky="nsew")
        self.rua_dados = tk.Frame(self.rua)
        self.rua_dados.pack(fill="both", expand=True)

        self.numero = tk.Frame(self)
        self.numero.grid(row=1, column=6, sticky="nsew")
        self.numero_dados = tk.Frame(self.numero)
        self.numero_dados.pack(fill="both", expand=True)

        self.complemento = tk.Frame(self)
        self.complemento.grid(row=1, column=7, sticky="nsew")
        self.complemento_dados = tk.Frame(self.complemento)
        self.complemento_dados.pack(fill="both", expand=True)

        self.bairro = tk.Frame(self)
        self.bairro.grid(row=1, column=8, sticky="nsew")
        self.bairro_dados = tk.Frame(self.bairro)
        self.bairro_dados.pack(fill="both", expand=True)

        self.cidade = tk.Frame(self)
        self.cidade.grid(row=1, column=9, sticky="nsew")
        self.cidade_dados = tk.Frame(self.cidade)
        self.cidade_dados.pack(fill="both", expand=True)

        self.uf = tk.Frame(self)
        self.uf.grid(row=1, column=10, sticky="nsew")
        self.uf_dados = tk.Frame(self.uf)
        self.uf_dados.pack(fill="both", expand=True)

        self.cep = tk.Frame(self)
        self.cep.grid(row=1, column=11, sticky="nsew")
        self.cep_dados = tk.Frame(self.cep)
        self.cep_dados.pack(fill="both", expand=True)

        self.contato = tk.Frame(self)
        self.contato.grid(row=1, column=12, sticky="nsew")
        self.contato_dados = tk.Frame(self.contato)
        self.contato_dados.pack(fill="both", expand=True)

        coluna_index = tk.Label(self.index,
                                text="idx",
                                font=("Arial", 10, "bold"))
        coluna_index.pack(pady=10)

        coluna_nome = tk.Label(self.nome,
                               text="nome",
                               font=("Arial", 10, "bold"))
        coluna_nome.pack(pady=10)

        coluna_cpf = tk.Label(self.cpf,
                              text="CPF",
                              font=("Arial", 10, "bold"))
        coluna_cpf.pack(pady=10)

        coluna_cnpj = tk.Label(self.cnpj,
                               text="CNPJ",
                               font=("Arial", 10, "bold"))
        coluna_cnpj.pack(pady=10)

        coluna_data = tk.Label(self.data,
                               text="data",
                               font=("Arial", 10, "bold"))
        coluna_data.pack(pady=10)

        coluna_rua = tk.Label(self.rua,
                              text="rua",
                              font=("Arial", 10, "bold"))
        coluna_rua.pack(pady=10)

        coluna_numero = tk.Label(self.numero,
                                 text="número",
                                 font=("Arial", 10, "bold"))
        coluna_numero.pack(pady=10)

        coluna_complemento = tk.Label(self.complemento,
                                      text="complemento",
                                      font=("Arial", 10, "bold"))
        coluna_complemento.pack(pady=10)

        coluna_bairro = tk.Label(self.bairro,
                                 text="bairro",
                                 font=("Arial", 10, "bold"))
        coluna_bairro.pack(pady=10)

        coluna_cidade = tk.Label(self.cidade,
                                 text="cidade",
                                 font=("Arial", 10, "bold"))
        coluna_cidade.pack(pady=10)

        coluna_uf = tk.Label(self.uf,
                             text="UF",
                             font=("Arial", 10, "bold"))
        coluna_uf.pack(pady=10)

        coluna_cep = tk.Label(self.cep,
                              text="CEP",
                              font=("Arial", 10, "bold"))
        coluna_cep.pack(pady=10)

        coluna_contato = tk.Label(self.contato,
                                  text="contato",
                                  font=("Arial", 10, "bold"))
        coluna_contato.pack(pady=10)

        self.botao = tk.Frame(self, width=600)
        self.botao.grid(row=2, column=0, columnspan=13, sticky="ew")

        campo_delete = tk.Label(self.botao,
                                text="Digite o idx do usuário de interesse",
                                font=("Arial", 14, "bold"))
        campo_delete.pack(pady=10, padx=10)

        self.campo_delete = tk.Entry(self.botao)
        self.campo_delete.pack(padx=(20, 20))

        self.botao_delete = tk.Button(self.botao,
                                      text="Deletar Usuário")

        self.botao_delete.pack(pady=10)

        self.botao_delete = tk.Button(self.botao,
                                      text="Atualizar Usuário")

        self.botao_delete.pack(pady=10)

        self.colunas_dados = [
            self.index_dados, self.nome_dados, self.cpf_dados, self.cnpj_dados,
            self.data_dados, self.rua_dados, self.numero_dados, self.complemento_dados,
            self.bairro_dados, self.cidade_dados, self.uf_dados, self.cep_dados,
            self.contato_dados
        ]
        self.atualizar_usuarios()

    def atualizar_usuarios(self):
        for coluna in self.colunas_dados:
            for widget in coluna.winfo_children():
                widget.destroy()

        users = self.controller.banco.Read()
        for user in users:
            for i, valor in enumerate(user):
                tk.Label(self.colunas_dados[i],
                         text=str(valor),
                         font=("Arial", 10)).pack(pady=5)


class TelaCadastro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # self.title("Catalogo de Prestadores de Serviço em Tecnologia da Informação (TI)")
        # self.geometry("900x600")

        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.controller = controller

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        titulo = tk.Label(self.titulo,
                          text="Cadastro",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        # LadoEsquerdo
        self.lado_esquerdo = tk.Frame(self, width=300)
        self.lado_esquerdo.grid(row=1, column=0, sticky="nsew")

        self.lado_direito = tk.Frame(self, width=300)
        self.lado_direito.grid(row=1, column=1, sticky="nsew", padx=30)

        # Preencher os lados

        self.construir_esquerda()
        self.construir_direita()

        # Botão Inferior
        self.contruir_botao(controller)

        self.tupla = (None, None, None, None, None, None, None, None, None, None, None)

    def construir_esquerda(self):
        # NOME
        nome = tk.Label(self.lado_esquerdo,
                        text="Nome",
                        font=("Arial", 14, "bold"))
        nome.pack(pady=10, padx=10)

        self.campo_nome = tk.Entry(self.lado_esquerdo)
        self.campo_nome.pack(padx=(20, 20))

        # CPF
        cpf = tk.Label(self.lado_esquerdo,
                       text="CPF ou CNPJ",
                       font=("Arial", 14, "bold"))
        cpf.pack(pady=10, padx=10)

        self.campo_cpf = tk.Entry(self.lado_esquerdo)
        self.campo_cpf.pack(padx=(20, 20))

        # NASCIMENTO
        nascimento = tk.Label(self.lado_esquerdo,
                              text="Data de Nascimento",
                              font=("Arial", 14, "bold"))
        nascimento.pack(pady=10, padx=10)

        # DATA
        campo_data = tk.Frame(self.lado_esquerdo)
        campo_data.pack(pady=5)
        self.dia = tk.Spinbox(campo_data,
                              from_=1, to=31,
                              width=4,
                              font=("Arial", 12))
        self.mes = tk.Spinbox(campo_data,
                              from_=1, to=12,
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

        self.campo_contato = tk.Entry(self.lado_esquerdo)
        self.campo_contato.pack(padx=(20, 20))

    def construir_direita(self):
        self.lado_direito.grid_columnconfigure(0, weight=1)
        self.lado_direito.grid_columnconfigure(1, weight=1)
        self.lado_direito.grid_rowconfigure(1, weight=1)

        frame_cep = tk.Frame(self.lado_direito, width=300)
        frame_cep.grid(row=0, column=0, columnspan=2, sticky="nsew")

        cep = tk.Label(frame_cep,
                       text="CEP",
                       font=("Arial", 14, "bold"))
        cep.pack(pady=10, padx=10)

        self.campo_cep = tk.Entry(frame_cep)
        self.campo_cep.pack(padx=(20, 20))

        # Subdivisão

        frame_esquerda = tk.Frame(self.lado_direito, width=150)
        frame_esquerda.grid(row=1, column=0, sticky="nsew")

        frame_direita = tk.Frame(self.lado_direito, width=150)
        frame_direita.grid(row=1, column=1, sticky="nsew")

        # Esquerda

        rua = tk.Label(frame_esquerda,
                       text="Rua",
                       font=("Arial", 14, "bold"))
        rua.pack(pady=10, padx=10)

        self.campo_rua = tk.Entry(frame_esquerda)
        self.campo_rua.pack(padx=(20, 20))

        numero = tk.Label(frame_esquerda,
                          text="Numero",
                          font=("Arial", 14, "bold"))
        numero.pack(pady=10, padx=10)

        self.campo_numero = tk.Entry(frame_esquerda)
        self.campo_numero.pack(padx=(20, 20))

        cidade = tk.Label(frame_esquerda,
                          text="Cidade",
                          font=("Arial", 14, "bold"))
        cidade.pack(pady=10, padx=10)

        self.campo_cidade = tk.Entry(frame_esquerda)
        self.campo_cidade.pack(padx=(20, 20))

        # Direita

        complemento = tk.Label(frame_direita,
                               text="Complemento",
                               font=("Arial", 14, "bold"))
        complemento.pack(pady=10, padx=10)

        self.campo_complemento = tk.Entry(frame_direita)
        self.campo_complemento.pack(padx=(20, 20))

        bairro = tk.Label(frame_direita,
                          text="Bairro",
                          font=("Arial", 14, "bold"))
        bairro.pack(pady=10, padx=10)

        self.campo_bairro = tk.Entry(frame_direita)
        self.campo_bairro.pack(padx=(20, 20))

        uf = tk.Label(frame_direita,
                      text="UF",
                      font=("Arial", 14, "bold"))
        uf.pack(pady=10, padx=10)

        self.campo_uf = tk.Entry(frame_direita)
        self.campo_uf.pack(padx=(20, 20))

    def adicionar_usuario(self):

        data_nascimento = self.dia.get() + "-" + self.mes.get() + "-" + self.ano.get()
        # print(data_nascimento)

        try:
            CheckValidCPF(self.campo_cpf.get())
            try:
                (rua, cidade, bairro, UF) = AdressInformation(self.campo_cep.get())
                self.controller.banco.Create(
                    self.campo_nome.get(),
                    self.campo_cpf.get(),
                    None,
                    data_nascimento,
                    rua,
                    self.campo_numero.get(),
                    self.campo_complemento.get(),
                    bairro,
                    cidade,
                    UF,
                    self.campo_cep.get(),
                    self.campo_contato.get())
                self.controller.mostrar_tela(TelaSucesso)
            except:
                self.controller.mostrar_tela(TelaErroCEP)

        except:
            try:
                CheckValidCNPJ(self.campo_cpf.get())
                try:
                    (rua, cidade, bairro, UF) = AdressInformation(self.campo_cep.get())
                    self.controller.banco.Create(
                        self.campo_nome.get(),
                        None,
                        self.campo_cpf.get(),
                        data_nascimento,
                        rua,
                        self.campo_numero.get(),
                        self.campo_complemento.get(),
                        bairro,
                        cidade,
                        UF,
                        self.campo_cep.get(),
                        self.campo_contato.get())
                    self.controller.mostrar_tela(TelaSucesso)
                except:
                    self.controller.mostrar_tela(TelaErroCEP)
            except:
                self.controller.mostrar_tela(TelaErroDocumento)

    def contruir_botao(self, controller):
        frame_botao_adicionar = tk.Frame(self, width=600)
        frame_botao_adicionar.grid(row=2, column=0, sticky="ew")

        self.botao_adicionar = tk.Button(frame_botao_adicionar,
                                         text="Adicionar Usuário",
                                         command=self.adicionar_usuario)

        self.botao_adicionar.pack(pady=10)

        frame_botao_ver_users = tk.Frame(self, width=600)
        frame_botao_ver_users.grid(row=2, column=1, sticky="ew")

        self.botao_ver_users = tk.Button(frame_botao_ver_users,
                                         text="Ver usuários",
                                         command=lambda: (
                                             controller.frames[TelaUsuarios].atualizar_usuarios(),
                                             controller.mostrar_tela(TelaUsuarios)
                                         ))

        self.botao_ver_users.pack(pady=10)

    def get_tupla(self):
        return self.tupla


class TelaErroDocumento(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        titulo = tk.Label(self.titulo,
                          text="Você digitou um CPF inválido",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        self.botao_erro = tk.Button(self,
                                    text="Clique para tentar novamente",
                                    command=lambda: controller.mostrar_tela(TelaCadastro))

        self.botao_erro.grid(row=1, column=0, columnspan=2, pady=10)


class TelaErroCEP(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        titulo = tk.Label(self.titulo,
                          text="Você digitou um CEP inválido",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        self.botao_erro = tk.Button(self,
                                    text="Clique para tentar novamente",
                                    command=lambda: controller.mostrar_tela(TelaCadastro))

        self.botao_erro.grid(row=1, column=0, columnspan=2, pady=10)


class TelaSucesso(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        titulo = tk.Label(self.titulo,
                          text="Usuário adicionado com sucesso",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        self.botao_erro = tk.Button(self,
                                    text="Adicionar novo usuário",
                                    command=lambda: controller.mostrar_tela(TelaCadastro))

        self.botao_erro.grid(row=1, column=0, columnspan=2, pady=10)


class TelaDeletado(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Divisão na Tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = tk.Frame(self, width=600)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        titulo = tk.Label(self.titulo,
                          text="Usuário deletado com sucesso",
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        self.botao_erro = tk.Button(self,
                                    text="Adicionar novo usuário",
                                    command=lambda: (
                                        controller.frames[TelaUsuarios].atualizar_usuarios(),
                                        controller.mostrar_tela(TelaUsuarios)
                                    ))

        self.botao_erro.grid(row=1, column=0, columnspan=2, pady=10)


