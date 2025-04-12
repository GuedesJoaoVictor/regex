from src.verificador import Verificador


def get_inputs():
    nome_produto = input("Digite o nome para o produto:")
    codigo = input("Digite o código do produto:")
    preco = input("Digite o preco do produto:")
    data = input("Digite a data de validade:")

    return nome_produto, codigo, preco, data


if __name__ == "__main__":
    nome_produto, codigo, preco, data = get_inputs()
    print(Verificador.verificador_nome_produto(nome_produto))
    print(Verificador.verificador_codigo(codigo))