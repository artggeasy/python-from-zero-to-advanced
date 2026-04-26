#Sistema Bibiolteca
def cadastrar_livro(biblioteca, titulo, autor, disponivel=True):
    if any(t["titulo"] == titulo for t in biblioteca):
        return 'Livro já cadstrado'
    else:
        biblioteca.append({"titulo": titulo, "autor":autor,"disponivel":disponivel})
        return "Livro Cadastrado com Sucesso!"
    
def buscar_por_autor(biblioteca, autor):
    livros = []
    for livro in biblioteca:
        if livro["autor"] == autor:
            livros.append(livro["titulo"])
    if not livros:
        return "Não há livros desse autor"
    return livros

def pegar_emprestado(biblioteca, titulo):
    for existe in biblioteca:
        if titulo == existe["titulo"]:
            if existe["disponivel"]!= False:
                existe["disponivel"] = False
                return "Empréstimo realizado"
            else:
                return "Livro Indisponivel"
    return "Não existe este livro"

def listar_disponiveis(biblioteca):
    disponiveis = [d["titulo"] for d in biblioteca if d["disponivel"]]
    if not disponiveis:
        return "Não há livros Disponiveis"
    return disponiveis
        
biblioteca = []

print(cadastrar_livro(biblioteca, "O Hobbit", "Tolkien"))
print(cadastrar_livro(biblioteca, "1984", "Orwell"))
print(cadastrar_livro(biblioteca, "O Hobbit", "Tolkien"))  # já cadastrado

print(buscar_por_autor(biblioteca, "Orwell"))   # ['1984']
print(buscar_por_autor(biblioteca, "Rowling"))  # Nenhum livro encontrado

print(pegar_emprestado(biblioteca, "O Hobbit"))  # Empréstimo realizado
print(pegar_emprestado(biblioteca, "O Hobbit"))  # Livro indisponível
print(pegar_emprestado(biblioteca, "Duna"))      # Livro não encontrado

print(listar_disponiveis(biblioteca))  # ['1984']