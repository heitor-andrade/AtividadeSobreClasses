class Investimento ():
    def __init__(self, sInicial, juros):
        self.sInicial = sInicial
        self.juros = 1 + juros / 100

    def adicionarJuros(self):
        self.sInicial *= self.juros
        
conta = Investimento(1000, 10)
for i in range (5):
    conta.adicionarJuros()
    print(conta.sInicial)