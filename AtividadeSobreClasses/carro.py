class Carro():
    def __init__(self, consumo, combustivel = 0):
        self.consumo = consumo
        self.combustivel = combustivel
        self.faltando = 0

    def andar(self, kilometros):
        consumo = kilometros / self.consumo
        self.combustivel = self.combustivel - consumo
        if self.combustivel < 0 :
            self.faltando = self.combustivel * -1
            self.combustivel = 0
            return 'falta ' + str(self.faltando) + ' litros' 
        return 'sobrou: ' + str(self.combustivel) + ' litros'

    def obterGasolina(self):
        return self.combustivel
    
    def adicionarGasolina(self, abastecido):
        self.combustivel += abastecido
        return self.combustivel

meuFusca = Carro(10, 10)

print(meuFusca.obterGasolina())

print (meuFusca.andar(1000))

print(meuFusca.obterGasolina())

print(meuFusca.adicionarGasolina(10))
