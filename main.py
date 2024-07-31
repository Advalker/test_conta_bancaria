class ContaBanco:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito    

    def saldo_em_conta(self):
        return self.saldo    