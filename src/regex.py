import re

class Regex:
    nome_produto = re.compile(r"(?x)^(?P<letra_maiuscula>[A-Z]) *"
                              r"(?P<primeira_palavra>[a-zA-Z0-9]*\s*) "
                              r"(?P<segunda_palavra>[a-zA-Z0-9]+\s*) "
                              r"(?P<terceira_palavra>[a-zA-Z0-9]+\s*)"
                              r"(?P<n_palavras>\s*([a-zA-Z0-9])*)*")
    codigo = re.compile(r"(?x)^(?P<letras>[A-Z]{6})"
                        r"(?P<numeros>[0-9]{4})$")
    preco = re.compile(
        r"(?x)^(?P<preco_virgula>([0-9]{1,3}\.)([0-9]{3}\.?)+,[0-9]{2})|"
        r"(?P<preco_ponto>([0-9]{1,3},)([0-9]{3},?)+\.[0-9]{2})|"
        r"(?P<preco>[0-9]+([.,])[0-9]{2})")
    datas = re.compile(
        r"(?x)^(?P<dias>(0[1-9])|([12][0-9])|(3[01]))/"
        r"(?P<meses>(0[1-9])|1[0-2])/"
        r"(?P<anos>(20([0-1][0-9]|2[0-5]))|(19[5-9][0-9]))$")

    @staticmethod
    def verifica_nome_produto(nome_produto):
        if Regex.nome_produto.search(nome_produto):
            return True
        return False

    @staticmethod
    def verifica_codigo(codigo):
        if Regex.codigo.search(codigo):
            return True
        return False

    @staticmethod
    def verifica_preco(preco):
        if Regex.preco.search(preco):
            return True
        return False

    @staticmethod
    def verifica_data(data):
        if Regex.datas.search(data):
            return True
        return False
