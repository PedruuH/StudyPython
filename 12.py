class Televisao():
    def __init__(self):
        self.canais={8:"globo",2:"SBT",10:"record",12:"band",26:"rede vida",4:"futura"}
        self.canalatual=0
        self.ligada= False
        self.volume= 20

    def ligar(self):
        self.ligada=True

    def desligar(self):
        self.ligada=False

    def mudarcanal(self,canal):
        self.canalatual=canal
        print("Canal atual: %s" % self.canais[canal])

    def aumenta_volume(self):
        self.volume += 1

    def abaixa_volume(self):
        self.volume -= 1
