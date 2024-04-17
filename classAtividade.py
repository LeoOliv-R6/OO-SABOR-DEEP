class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, nota_avaliacao=4.5):   
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
    
    
restaurante_exemplo = Restaurante(nome = 'Sabor DeeP', categoria = 'gourmet', ativo = True, capacidade = 50, nota_avaliacao = 5)

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, nota_avaliacao=4.5):   
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        
novo_restaurante = Restaurante(nome = 'Big Marmitas', categoria = 'boteco')

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, nota_avaliacao=4.5):   
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
restaurante_formatado = Restaurante(nome= 'Boanapetit', categoria= 'comida francesa')
print(restaurante_formatado)

class Cliente:
    def __init__(self, cpf='', rg='', nome='', idade=0):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.idade = idade
        
cliente1 = Cliente(cpf='11122233344', rg='123456789', nome='Joabe', idade='48')
cliente2 = Cliente(cpf='11122233355', rg='123456788', nome='Jobson', idade='49')
cliente3 = Cliente(cpf='11122233366', rg='123456787', nome='Jozias', idade='50')
