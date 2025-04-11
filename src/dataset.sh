dados_produtos = [
    # Totalmente válidos
    {
        "nome": "Camiseta Polo Masculina",
        "codigo": "ABCDEF1234",
        "preco": "99.99",
        "validade": "15/12/2025"
    },
    {
        "nome": "Tênis Esportivo Masculino",
        "codigo": "ZXCVBN5678",
        "preco": "149,90",
        "validade": "01/01/2026"
    },
    {
        "nome": "Bermuda Jeans Masculina",
        "codigo": "QWERTY0001",
        "preco": "79.9",
        "validade": "31/10/2025"
    },
    {
        "nome": "Vestido Longo Estampado",
        "codigo": "LONGDR1234",
        "preco": "120.00",
        "validade": "28/02/2024"  # válido (ano bissexto)
    },

    # Inválidos
    {
        "nome": "camiseta polo masculina",  # minúsculas
        "codigo": "abcdef1234",             # minúsculas
        "preco": "99.999",                  # 3 casas decimais
        "validade": "15/12/25"              # ano com 2 dígitos
    },
    {
        "nome": "Camisa Masculina",         # menos de 3 palavras
        "codigo": "ABC1234@",               # caractere especial
        "preco": "-49,90",                  # valor negativo
        "validade": "32/12/2025"            # dia inválido
    },
    {
        "nome": "Calça Jeans Slim",
        "codigo": "ABCDE1234",              # só 5 letras
        "preco": "100,999",                 # 3 casas decimais
        "validade": "30-12-2025"            # separadores errados
    },
    {
        "nome": "Blusa De Frio",
        "codigo": "1234567890",             # só números
        "preco": "0.00",
        "validade": "00/00/0000"            # tudo inválido
    },
    {
        "nome": "Jaqueta Masculina Couro",
        "codigo": "C0D1C01234",             # contém números entre letras
        "preco": "abc",                     # não é número
        "validade": "31/04/2025"            # abril não tem 31 dias (invalidez lógica)
    },
    {
        "nome": "Boné Vermelho Casual",
        "codigo": "VERMEL0000",
        "preco": "199",                     # inteiro, mas válido
        "validade": "29/02/2023"            # 2023 não é bissexto
    },
    {
        "nome": "Mochila Escolar Grande",
        "codigo": "MOCHIL123",              # só 3 dígitos
        "preco": "250.5",                   # 1 casa decimal (válido)
        "validade": "12/13/2025"            # mês inválido
    },
    {
        "nome": "Tênis Corrida Branco",
        "codigo": "RUNSHO1234",
        "preco": "300,00",
        "validade": "15/06/2030"
    }
]
