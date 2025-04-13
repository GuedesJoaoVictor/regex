import re

class Regex:
    """
    Classe Regex
    Responsável por armazenar as expressões regulares utilizadas no sistema.
    """
    nome_produto = re.compile(
        r"^(?P<nome>([A-Z] ?[a-zA-Z0-9]+)(\s+[a-zA-Z0-9]+){2,} *)$"
    )

    codigo = re.compile(r"(?x)^(?P<letras>[A-Z]{6})"
                        r"(?P<numeros>[0-9]{4})$")
    preco = re.compile(
        r"(?xm)^(?P<preco_virgula>([0-9]{1,3}\.)([0-9]{3}\.?)+,[0-9]{2})|"
        r"(?P<preco_ponto>([0-9]{1,3},)([0-9]{3},?)+\.[0-9]{2})|"
        r"(?P<preco>[0-9]+([.,])[0-9]{2})")
    datas = re.compile(
        r"(?xm)^(?P<dias>(0[1-9])|([12][0-9])|(3[01]))/"
        r"(?P<meses>(0[1-9])|1[0-2])/"
        r"(?P<anos>(20([0-1][0-9]|2[0-5]))|(19[5-9][0-9]))$")

    # Metodo estatico para verificar se o nome do produto é valido
    # Formato Camiseta confortavel G
    @staticmethod
    def verifica_nome_produto(nome_produto):
        if Regex.nome_produto.search(nome_produto):
            return True
        return False

    # Metodo estatico para verificar se o codigo do produto é valido
    # Formato ABCDEF1234
    @staticmethod
    def verifica_codigo(codigo):
        if Regex.codigo.search(codigo):
            return True
        return False

    # Metodo estatico para verificar se o preco do produto é valido
    # Formatos: 1.000,00 | 100,000.00 | 99,99 | 10.99
    @staticmethod
    def verifica_preco(preco):
        if Regex.preco.search(preco):
            return True
        return False

    # Metodo estatico para verificar se a data de validade do produto é valida
    # Formato: dd/mm/aaaa
    @staticmethod
    def verifica_data(data):
        if Regex.datas.search(data):
            return True
        return False
