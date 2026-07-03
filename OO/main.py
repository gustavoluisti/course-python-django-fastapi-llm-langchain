class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacao(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def calculadora(self, v1, v2):
        soma = v1 + v2
        return print(f"A soma de {v1} com {v2} é igual a {soma}")
        

celular = Celular()

print(celular.marca)
celular.fazer_ligacao()
celular.jogar_cobrinha()
celular.calculadora(5, 5)