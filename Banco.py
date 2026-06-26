import sqlite3

def CheckValidCPF(CPF):
    return True

def CheckValidCNPJ(CNPJ):
    return True

def AdressInformation(CEP):
    rua = None
    numero = None
    complemento = None
    bairro = None
    UF = None
    return (rua, numero, complemento, bairro, UF)


class Banco:
    def __init__(self, caminho_banco="users.db"):
        self.conexao = sqlite3.connect(caminho_banco)
        self.CreateTable()

    def CreateTable(self):
        c = self.conexao.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                CPF TEXT,
                CNPJ TEXT,
                dataNascimento TEXT,
                rua TEXT,
                numero TEXT,
                complemento TEXT,
                bairro TEXT,
                UF TEXT,
                CEP TEXT
            )
            """
        )
        self.conexao.commit()
        c.close()

    def Create(
        self,
        nome,
        CPF=None,
        CNPJ=None,
        dataNascimento=None,
        rua=None,
        numero=None,
        complemento=None,
        bairro=None,
        UF=None,
        CEP=None,
    ):
        c = self.conexao.cursor()

        if CheckValidCPF(CPF):
            CPF: str = CPF
            CNPJ = None
        elif CheckValidCNPJ(CNPJ):
            CNPJ: str = CNPJ
            CPF = None
        else:
            print("CPF ou CNPJ inválido")

        (rua, numero, complemento, bairro, UF) = AdressInformation(CEP)

        c.execute(
            """
            INSERT INTO users (
                nome, CPF, CNPJ, dataNascimento, rua, numero, complemento, bairro, UF, CEP
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,(nome, CPF, CNPJ, dataNascimento, rua, numero, complemento, bairro, UF, CEP),)
        self.conexao.commit()
        newID = c.lastrowid
        c.close()
        return newID

    def Read(self):
        c = self.conexao.cursor()
        c.execute("SELECT id, nome FROM users ORDER BY id")
        users = c.fetchall()
        c.close()
        return users

    def Update(self, Id,
        nome = None,
        CPF=None,
        CNPJ=None,
        dataNascimento=None,
        rua=None,
        numero=None,
        complemento=None,
        bairro=None,
        UF=None,
        CEP=None,
    ):
        c = self.conexao.cursor()

        if CheckValidCPF(CPF):
            CPF: str = CPF
            CNPJ = None
        elif CheckValidCNPJ(CNPJ):
            CNPJ: str = CNPJ
            CPF = None
        else:
            print("CPF ou CNPJ inválido")

        (rua, numero, complemento, bairro, UF) = AdressInformation(CEP)

        c.execute(
            """
            UPDATE users
            SET nome = ?,
                CPF = ?,
                CNPJ = ?,
                dataNascimento = ?,
                rua = ?,
                numero = ?,
                complemento = ?,
                bairro = ?,
                UF = ?,
                CEP = ?
            WHERE id = ?
            """,
            (nome, CPF, CNPJ, dataNascimento, rua, numero, complemento, bairro, UF, CEP, id),
        )
        self.conexao.commit()
        c.close()

    def Delete(self, Id):
        c = self.conexao.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conexao.commit()
        c.close()

