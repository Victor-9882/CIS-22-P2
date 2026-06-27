import tkinter as tk


class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Catalogo de Prestadores de Serviço em Tecnologia da Informação (TI)")
        self.geometry("900x600")



        # Divisão na Tela
        self.grid_rowconfigure(0, weight=1)

        #LadoEsquerdo
        self.lado_esquerdo = tk.Frame(self, width = 300)
        self.lado_esquerdo.grid(row=0, column=0, sticky="nsew")

        self.lado_direito = tk.Frame(self, width = 300)
        self.lado_direito.grid(row=0, column=1, sticky="nsew", padx= 10)

        #Preencher os lados

        self.construir_esquerda()

        self.construir_direita()


    def construir_esquerda(self):
        titulo = tk.Label(self.lado_esquerdo, 
                          text="Aaa")
        titulo.pack()


    def construir_direita(self):
        titulo = tk.Label(self.lado_direito, 
                          text="Aaa")
        titulo.pack()


janela = Aplicativo()
janela.mainloop()