class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        # None deixa a variável default sem valor, permitindo que instancie
        # com atributo sem valor
        self.nome = nome
        self.idade = int(idade)
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa(nome='João', idade=17)
    pedro = Pessoa(joao, nome='Pedro', idade=45)
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
