def processar_pagamento(pagamento):
    if valor<0: raise ValueError("Error: Valor não pode ser Negativo")
    if not valor:raise ValueError("Error: Valor não pode ser vazio")
    try:
        valor = float(pagamento)
    except ValueError as e:
        print(f"Error capturado: {e}")
    

print(processar_pagamento({"valor":"150.00"}))
print(processar_pagamento({"valor": "abc"}))
print(processar_pagamento({"valor": -50}))     
print(processar_pagamento({"taxa": 10}))