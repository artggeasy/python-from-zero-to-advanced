def adicionar_contato(contatos, nome, telefone):
    if any(c["nome"] == nome for c in contatos):
        return "Contato já cadastrado"
    contatos.append({"nome": nome, "telefone": telefone})
    return "Contato adicionado"

def buscar_contato(contatos, nome):
    for contato in contatos:
        if contato["nome"] == nome:
            return contato
    return "Contato não encontrado"

def listar_contatos(contatos):
    if not contatos:
        return "Nenhum contato cadastrado"
    return [c["nome"] for c in contatos]


contatos = []
print(adicionar_contato(contatos, "Arthur", "99999-0001"))
print(adicionar_contato(contatos, "Sabrina", "99999-0002"))
print(adicionar_contato(contatos, "Arthur", "99999-0003"))
print(buscar_contato(contatos, "Sabrina"))
print(buscar_contato(contatos, "Lucas"))
print(listar_contatos(contatos))