'''
escrever uma função fizzbuzz()
se for multiplo de 2 printa fizz e multiplos de 5 print buzz
'''

def fizzbuzz(n):
    pass
    for i in range(n):
        if  (i + 1) % 2 == 0 and (i + 1) % 5 == 0:
            print('fizzbuzz')
        elif (i + 1) % 5 == 0:
            print('buzz')
        elif (i + 1) % 2 == 0:
            print('fizz')
        else:
            print(i + 1)

if __name__ == "__main__":
    n = int(input('Blá blá blá só numeros: '))

    fizzbuzz(n)
