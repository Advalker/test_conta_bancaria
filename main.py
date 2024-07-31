class ContaBanco:

    def __init__(self, nome, saldo = 0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito    

    def saldo_em_conta(self):
        return self.saldo    
    
    def sacar(self, saldo):
        if saldo <= self.saldo:
            self.saldo = self.saldo - saldo
            return self.saldo
        else:
            print(f"Saldo insuficiente! Seu saldo é de {self.saldo}.")


conta = ContaBanco("valker") 
conta.depositar(200)
print(conta.saldo_em_conta())    
conta.sacar(50)
print(conta.saldo_em_conta())     
conta.sacar(250)
  