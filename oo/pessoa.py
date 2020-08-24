class Pessoa:
    olhos = 2 # atributo de classe, reserva o mesmo lugar na memória
    # para todos os objetos com o valor defaut

    def __init__(self, *filhos, nome=None, idade=0):
        # None deixa a variável default sem valor, permitindo
        # que instancie com atributo sem valor
        self.nome = str(nome)
        self.idade = int(idade)
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod # decorator
    def metodo_estatico():
        return 42

    @classmethod # decorator
    def nome_e_atributos_de_classe(cls):
        return f'{cls} = olhos{cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    joao = Homem(nome='João', idade=17)
    pedro = Homem(joao, nome='Pedro', idade=45)
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    pedro.sobrenome = 'Alves'
    # add um atributo dinâmico

    del joao.filhos
    # 'del' deleta atributos de classes dinamicamente mas não
    # é uma boa prática, prefere-se que coloque na iniciação

    print(joao.__dict__)
    print(pedro.__dict__)
    # __dict__ printa no console os atributos de instancia
    # e dinamicos de cada classe
    print(Pessoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe())
    pessoa = Pessoa('anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(pedro, Pessoa))
    print(isinstance(pedro, Homem))
