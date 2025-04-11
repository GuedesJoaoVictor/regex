from src.regex import Regex

class Verificador:
    @staticmethod
    def verificador_nome_produto(nome_produto):
        """
        Verifica se o nome do produto é válido.
        :param nome_produto: Nome do produto a ser verificado.
        :return: True se o nome do produto for válido, False caso contrário.
        """
        if Regex.verifica_nome_produto(nome_produto):
            return True
        return False