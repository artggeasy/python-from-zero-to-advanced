#Sistema Escola
def matricular(alunos,nome,curso):
    if any (a["nome"] == nome for a in alunos):
        return "Aluno já cadastrado"
    else: 
        alunos.append({"nome":nome,"curso":curso,"notas":[]})
        return 'Cadastro feito com sucesso!'

def lancar_nota(alunos, nome, nota):
    for aluno in alunos:
        if aluno["nome"] == nome:
            if nota < 0 or nota > 10:
                return "Nota inválida"
            aluno["notas"].append(nota)
            return "Nota lançada com sucesso"
    return "Aluno não encontrado"
    
def media(alunos, nome):
    nota = []
    media = 0
    for aluno in alunos:
        if aluno["nome"] == nome:
            if not aluno["notas"]:
                return "Aluno sem notas"
            else:
                nota = aluno["notas"]
                media = sum(nota)/len(nota)
                return f"{aluno["nome"]} Média: {media:.2f}"
            
    if not any(a["nome"] == nome for a in alunos):
        return "Aluno inexistente"
def aprovados(alunos):
    resultado = []
    for aluno in alunos:
        if not aluno["notas"]:
            continue
        m = sum(aluno["notas"]) / len(aluno["notas"])
        if m >= 6:
            resultado.append(aluno["nome"])
    return resultado


alunos = []

print(matricular(alunos, "Arthur", "Backend"))
print(matricular(alunos, "Sabrina", "Frontend"))
print(matricular(alunos, "Arthur", "Backend"))   # já matriculado

print(lancar_nota(alunos, "Arthur", 8))
print(lancar_nota(alunos, "Arthur", 6))
print(lancar_nota(alunos, "Arthur", 11))         # nota inválida
print(lancar_nota(alunos, "Lucas", 9))           # não encontrado

print(media(alunos, "Arthur"))    # Média de Arthur: 7.00
print(media(alunos, "Sabrina"))   # Sem notas lançadas

print(aprovados(alunos))          # ['Arthur']
            


    