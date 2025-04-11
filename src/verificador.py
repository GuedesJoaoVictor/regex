from src.regex import Regex
import re

class Verificador:
    @staticmethod
    def verificador_nome_produto(nome_produto):
        """
        Verifica se o nome do produto é válido.
        :param nome_produto: Nome do produto a ser verificado.
        :return: True se o nome do produto for válido, False caso contrário.
        """
        if Regex.verifica_nome_produto(nome_produto):
            print("Nome do produto válido.")
            return True
        else:
            regex_primeira_letra = re.compile(r"^[a-z]")
            if regex_primeira_letra.match(nome_produto):
                nome_produto[0] = nome_produto[0].upper()
                print(nome_produto)
                return Verificador.verificador_nome_produto(nome_produto)
            else:
                print("Nome do produto não começa com uma letra.")
                return False