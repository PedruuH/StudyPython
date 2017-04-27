class Bus():
    def __init__(self):
        self.cor = 'Amarelo'
        self.lugares = 100
        self.velocidade = 0

    def acelera(self, aumento):
        self.velocidade += aumento*aumento

    def para(self):
        self.velocidade = 0

