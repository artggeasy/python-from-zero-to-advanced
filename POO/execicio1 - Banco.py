class ContaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0
    
    def deposito (self, valor):
        self.saldo += valor
        
    def sacar (self, valor):
        if self.saldo < valor: print("Saldo insuficiente")
        else:
            self.saldo -= valor
    
    def extrato(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}"
    
conta = ContaBancaria("João")
conta.deposito(1000)
conta.sacar(300)
conta.sacar(800)
print(conta.extrato())