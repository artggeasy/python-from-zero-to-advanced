def saudacao():
    return 'Olá Mundo'
def saudacoes(nome):
    return f'Olá {nome}'
def soma(a, b):
    return a + b
def verifica_idade(idade):
    if idade>=18:
        return 'Você é maior de idade!'
    else:
        return 'Você é menor de idade!'
#Função sem parâmetro
print(saudacao())
#função com parâmetro
print(saudacoes('Arthur'))
#Função com mais de um parâmetro
print(f'A Soma de 2 e 3 é {soma(2, 3)}')
#Função Verifica Idade
idade = int(input("Digite a sua Idade: "))
print(verifica_idade(idade))