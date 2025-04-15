from src.verificador import Verificador


def get_inputs():
    nome_produto = input("Digite o nome para o produto no formato Alguma coisa G:")
    codigo = input("Digite o código do produto no formato ABCDEF1234:")
    preco = input("Digite o preco do produto:")
    data = input("Digite a data de validade dd/mm/aaaa:")

    return nome_produto, codigo, preco, data


if __name__ == "__main__":
    nome_produto, codigo, preco, data = get_inputs()
    print(Verificador.verificador_nome_produto(nome_produto))
    print(Verificador.verificador_codigo(codigo))
    print(Verificador.verificador_preco(preco))
    print(Verificador.verificador_data(data))