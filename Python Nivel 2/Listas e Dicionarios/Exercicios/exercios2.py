def resumo_usuario(usuario):
    return f"{usuario["Nome"]} tem {usuario["Idade"]} anos e mora em {usuario["Cidade"]}"


usuario1 = {"Nome":"Arthur","Idade":22,"Cidade":"Caxias"}
usuario2 = {"Nome":"Sabrina","Idade": 20,"Cidade":"Açailandia"}

print(resumo_usuario(usuario1))
print(resumo_usuario(usuario2))


