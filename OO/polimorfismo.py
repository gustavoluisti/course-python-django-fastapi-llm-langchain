class Animal:

    def emitir_som(self):
        print('Qualquer som...')

class Cachorro(Animal):
    pass
    def emitir_som(self):
        print('Au au')

class Gato(Cachorro):

    def emitir_som(self):
        print('Miau miau')

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()