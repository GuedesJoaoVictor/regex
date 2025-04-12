from random import randint

from regex import Regex
import re

class Verificador:
    letras = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z",
    }

    @staticmethod
    def verificador_nome_produto(nome_produto: str):
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
                nome_produto = nome_produto[0].upper() + nome_produto[1:]
                print(nome_produto)
                return Regex.verifica_nome_produto(nome_produto)
            else:
                # Fazer com que a primeira letra vire uma letra
                nome_produto = "A "+ nome_produto
                print(nome_produto)
                return Regex.verifica_nome_produto(nome_produto)
    @staticmethod
    def verificador_codigo(codigo: str):
        """
        Verifica se o código é válido.
        :param codigo: string a ser verificada, devendo estar no formato ABCEF1234
        :return: True se a string for válida, False caso contrario
        """
        if Regex.verifica_codigo(codigo):
            print("Codigo do produto válido")
            return True
        else:
            codigo = codigo.upper()
            # Converteremos a string em lista para modificar
            codigo_list = list(codigo)

            # Preenche ou corrige os primeiros caracteres
            for i in range(6):
                if i>= len(codigo_list) or not codigo_list[i].isalpha():
                    # Gera uma letra alaeatoria caso o caractere nao seja valido
                    codigo_list.insert(i, Verificador.letras[randint(0, 25)])
                    # Remove o proximo elemento pois como acabamos de adicionar uma letra na posição i
                    # o proximo elemento da lista é um numero.
                    codigo_list.remove(codigo_list[i + 1])

            # Completa os 4 ultimos digitos se for preciso
            for i in range(6, 10):
                # Se i >= ao tamanho da lista || codigo na posição i for uma letra
                if i >= len(codigo_list) or codigo_list[i].isalnum():
                    # Então trocamos a letra por um numero
                    codigo_list[i] = str(randint(0, 9))

            # Junta a lista em string
            novo_codigo = "".join(codigo_list[:10])
            print("Codigo corrigido: " + novo_codigo)
            return Regex.verifica_codigo(novo_codigo)