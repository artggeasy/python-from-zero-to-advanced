#Sistema de Academia

def cadastrar_aluno(alunos, nome, plano):
    if any (a["nome"] == nome for a in alunos):
        return 'Alunos já Cadastrado'
    else:
        if plano in ["vip", "premium", "basic"]:
            alunos.append({"nome":nome,"plano":plano,"treinos":[]})
            return 'Cadastro Concluido'
        else:
            return 'Plano Inválido'

def registrar_treino(alunos, nome, exercicio, duracao_min):
    for aluno in alunos:
        if aluno["nome"] == nome:
            if duracao_min <10:
                return 'Duração Inválida'
            else:
                aluno["treinos"].append({"Execicio":exercicio, "duração_min": duracao_min})
                return "Treino registrado"
    return "Aluno não encontrado"

def total_minutos(alunos, nome):
    total=0
    for aluno in alunos:
        if aluno["nome"] == nome:
            if not aluno["treinos"]:
                return 'Nenhum treino registrado'
            else:
                total = sum(d["duração_min"] for d in aluno["treinos"])
                return f"{aluno["nome"]} treinou {total} minutos no total"
    return "Aluno não encontrado"

def alunos_por_plano(alunos, plano):
    alunos_plano = []
    for aluno in alunos:
        if aluno["plano"] == plano:
            alunos_plano.append(aluno["nome"])
    if not alunos_plano:
        return "Nenhum aluno nesse plano"
    return alunos_plano

alunos = []

print(cadastrar_aluno(alunos, "Arthur", "premium"))
print(cadastrar_aluno(alunos, "Sabrina", "vip"))
print(cadastrar_aluno(alunos, "Arthur", "basic"))    # já cadastrado
print(cadastrar_aluno(alunos, "Lucas", "gold"))      # plano inválido

print(registrar_treino(alunos, "Arthur", "Supino", 60))
print(registrar_treino(alunos, "Arthur", "Agachamento", 45))
print(registrar_treino(alunos, "Arthur", "Caminhada", 5))   # duração inválida
print(registrar_treino(alunos, "Lucas", "Corrida", 30))     # não encontrado

print(total_minutos(alunos, "Arthur"))    # Arthur treinou 105 minutos no total
print(total_minutos(alunos, "Sabrina"))   # Nenhum treino registrado
print(total_minutos(alunos, "Lucas"))     # Aluno não encontrado

print(alunos_por_plano(alunos, "premium"))   # ['Arthur']
print(alunos_por_plano(alunos, "gold"))      # Nenhum aluno nesse plano
    


    
        