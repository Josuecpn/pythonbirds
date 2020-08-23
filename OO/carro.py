'''
crie uma classe que vai possuir dois atributos compostos por
outras por outras duas classes:

1) Motor:
controla velocidade e oferece os seguintes atributos:
1. atributo de dado velocidade
2. método acelerar, incrementa 1 ponto de velocidade
3. método frear, decrementa 2 pontos de velocidade

2) Direção:
controla a direção e oferece os seguintes atributos:
1. valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2. método girar_a_direita
3. método girar_a_esquerda

3)Carro:
vai ser composto por direção e motor ex.: Carro(direcao, motor)
e oferece os seguintes métodos:
calcular_velocidade, mostra a velocidade
calcular_direcao, mostra a direção

'''

class Motor:
    velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
    direcoes = ('Norte', 'Leste', 'Sul', 'Oeste')
    direcao = direcoes[0]
    n = 0

    def girar_a_direita(self):
        if self.n == 3:
            self.n -= 3
        else:
            self.n += 1

        self.direcao = self.direcoes[self.n]
        return self.direcao

    def girar_a_esquerda(self):
        if self.n == -4:
            self.n += 4
        else:
            self.n -= 1
        self.direcao = self.direcoes[self.n]
        return self.direcao

class Carro(Motor, Direcao):

    def calcular_direcao(self):
        print(self.direcao)

    def calcular_velocidade(self):
        print(self.velocidade)

        

if __name__ == '__main__':
    carro = Carro()

    carro.acelerar()
    carro.calcular_velocidade()

    carro.calcular_direcao()

    carro.acelerar()
    carro.calcular_velocidade()

    carro.girar_a_esquerda()
    carro.calcular_direcao()

    carro.acelerar()
    carro.calcular_velocidade()

    carro.girar_a_direita()
    carro.girar_a_direita()
    carro.calcular_direcao()

    carro.frear()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
