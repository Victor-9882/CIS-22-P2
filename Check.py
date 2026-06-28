import json
from validate_docbr import CPF, CNPJ
from urllib.request import Request, urlopen

def CheckValidCPF(CPF):
    cpf = CPF()
    return cpf.validate(CPF)

def CheckValidCNPJ(CNPJ):
    cnpj = CNPJ()
    return cnpj.validate(CNPJ)

def AdressInformation(CEP):
    cep = str(CEP).replace("-", "").replace(".", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP inválido")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    resposta = urlopen(request)
    dados = resposta.read().decode("utf-8")

    values = json.loads(dados)

    if "erro" in values:
        raise ValueError("CEP não encontrado")

    rua = values["logradouro"]
    complemento = values["complemento"]
    bairro = values["bairro"]
    UF = values["uf"]

    return (rua, complemento, bairro, UF)