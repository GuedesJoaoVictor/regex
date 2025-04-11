from src.regex import Regex

print(Regex.verifica_nome_produto("Produto Teste 1"))

def get_inputs():
    nome_produto = input(str("Digite o nome para o produto:"))
    codigo = input(str("Digite o código do produto:"))
    preco = input(str("Digite o preco do produto:"))
    data = input(str("Digite a data de validade:"))

    return nome_produto, codigo, preco, data

nome_produto, codigo, preco, data = get_inputs()
