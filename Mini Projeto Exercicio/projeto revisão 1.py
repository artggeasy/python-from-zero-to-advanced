class Pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.status = "aberto"

    def adicionar_item(self, nome, preco, quantidade):
        self.itens.append({"nome": nome, "preco": preco, "quantidade": quantidade})

    def total(self):
        return sum(item["preco"] * item["quantidade"] for item in self.itens)

    def fechar(self):
        self.status = "fechado"

    def resumo(self):
        linhas_itens = "\n".join(
            f"  - {item['quantidade']}x {item['nome']} R${item['preco']:.2f} cada"
            for item in self.itens
        )
        return (
            f"Cliente: {self.cliente}\n"
            f"Status: {self.status}\n"
            f"Itens:\n{linhas_itens}\n"
            f"Total: R${self.total():.2f}"
        )


def processar_pedido(pedido):
    if not pedido.itens:
        return "Erro: pedido sem itens"
    if pedido.status == "fechado":
        return "Erro: pedido já fechado"
    pedido.fechar()
    return pedido.resumo()


p = Pedido("Arthur")
print(processar_pedido(p))

p.adicionar_item("Pizza", 45.00, 2)
p.adicionar_item("Suco", 12.00, 1)
print(processar_pedido(p))

print(processar_pedido(p))