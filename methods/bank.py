class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False #_ protege o atributo
        
    def __str__(self):
        return f'Olá {self.titulat}, seu saldo é de {self.saldo}'
    
conta1 = ContaBancaria("Hope", 4299)
conta2 = ContaBancaria("Persy", 1333)

print(conta1)
print(conta2)

@classmethod
def ativar_conta(cls, conta):
    conta._ativo = True

conta3 = ContaBancaria("Pip", 2000)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

class ContaBancariaPy:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta4 = ContaBancariaPy("Leonardo", 10000)
print(f"Titular da conta 4: {conta4.titular}")

class ClienteBanco:
    def __init__(self, nome, idade, cep, cpf, profissao):
        self.nome= nome
        self.idade= idade
        self.cep= cep
        self.cpf= cpf
        self.profissao= profissao
        
cliente1 = ClienteBanco("Victor", 24, "01223450", "12345678900", "Dev Frontend")
cliente1 = ClienteBanco("Leonardo", 21, "01223550", "12345678901", "Dev Backend")
cliente1 = ClienteBanco("Gabriel", 24, "01223440", "12345678902", "Dev FullStack")

class ClienteBanco:
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPy(titular, saldo_inicial)
        return conta
    
conta_cliente1 = ClienteBanco.criar_conta("Nicole", 90000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")






