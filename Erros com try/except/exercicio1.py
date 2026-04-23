def processar_pagamento(pagamento):
    if "valor" not in pagamento:return "Erro; campo valor ausente"
    try:valor = float(pagamento["valor"])
    except ValueError: print("Erro: valor inválido")
    if valor<=0:return "Erro: valor deve ser positivo"
    return f"Pagamento de R${valor:.2f} aprovado"
print(processar_pagamento({"valor":"150.00"}))
