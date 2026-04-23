pedidos = [
    {"id": 1, "cliente": "Arthur", "valor": 520.00, "status": "entregue"},
    {"id": 2, "cliente": "Sabrina", "valor": 85.00, "status": "pendente"},
    {"id": 3, "cliente": "Lucas", "valor": 1300.00, "status": "entregue"},
    {"id": 4, "cliente": "Maria", "valor": 210.00, "status": "cancelado"},
    {"id": 5, "cliente": "João", "valor": 95.00, "status": "pendente"},
    {"id": 6, "cliente": "Fernanda", "valor": 740.00, "status": "entregue"},
]
entregues = [p['cliente'] for p in pedidos if p['status'] =="entregue"]
taxado = [{"cliente":p['cliente'], "valor":(p['valor']*1.05)} for p in pedidos if p['status'] == "pendente"]
ids = [p['id'] for p in pedidos if p['valor'] >500.0]
status_clientes = {p['cliente'] : p['status'] for p in pedidos}
print(entregues)
print(ids)
print(taxado)
print(status_clientes)

