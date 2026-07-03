class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5
    numero_portas = 4

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')

    def ligar(self):
        print(f'Ligando o carro...')

class i30(Carro):
    
    marca = 'Hyunday'
    ano = 2012
    modelo = 'i30'

    def ligar(self):
        print(f"Ligando o {self.modelo}")

carro = i30()
carro.ligar()