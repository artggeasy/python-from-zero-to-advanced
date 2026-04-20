nome = ["Arthur","Hiago","Joao"]
for i in(nome):
    print(i)
    
#exercicio 2
usuario = {"Nome":"Ana","Idade":20},{"Nome":"Carlos","Idade": 30}
for i in usuario:
    print(i["Nome"],"tem",i["Idade"],"anos")

#Mini Desafio
usuarios = {"Nome":"Arthur","Idade":22},{"Nome":"Daniel","Idade": 18},{"Nome":"Juan","Idade": 15},{"Nome":"Carla","Idade": 12}
for i in usuarios:
    if(i["Idade"]>=18):
        print(i["Nome"],"é de maior")
    else:
        print(i["Nome"],"é de menor")