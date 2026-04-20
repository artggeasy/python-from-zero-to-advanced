def verifica(idade):
    if idade>=18:
        return "Adulto!"
    if idade <= 12:
        return "Criança!"
    else:
        return "Adolescente!"
idade = int(input("Digite sua idade: "))  
print(verifica(idade))  