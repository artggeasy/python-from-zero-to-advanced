produtos = [
    {"nome": "Notebook", "preco": 3500, "disponivel": True},
    {"nome": "Mouse", "preco": 150, "disponivel": False},
    {"nome": "Teclado", "preco": 300, "disponivel": True},
    {"nome": "Monitor", "preco": 1200, "disponivel": True},
    {"nome": "Headset", "preco": 250, "disponivel": False},
]
disponiveis = [u['nome'] for u in produtos if u['disponivel']]
preco_menor = [u['nome'] for u in produtos if u['preco']<=400]
print(f"Produtos Disponiveis: {disponiveis}")
print(f"Produto com preço a baixo de 400R$: {preco_menor}")

lista = [{"nome":p['nome'],"preco":(p['preco']*0.9)} for p in produtos if p['disponivel']]
print(lista)


