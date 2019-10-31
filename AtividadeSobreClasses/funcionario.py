class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def rNome (self):
        return self.nome
    
    def rSalario (self):
        return self.salario

    def teste (self):
        print(self.nome)
        print(self.salario)

    def aSalario(self, juros):
        juros = juros/100 + 1
        self.salario *= juros
    
tortuga = Funcionario("tortuga", 25000)
tortuga.aSalario(10)
tortuga.teste()