class Pessoa:
    def __init__(self, nome=None, idade=int(0)):
        # None deixa a variável default sem valor, permitindo que instancie
        # com atributo sem valor
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa(nome='Pedro',idade=25)
    p2 = Pessoa('João', 27)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    print(p2.cumprimentar())
    print(p2.nome)
    print(p2.idade)
