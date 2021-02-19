"""LER UM NÚMERO E MOSTRAR O SEU SUCESSOR E SEU ANTECESSOR"""


def main():
    n1 = int(input('Digite um número : '))
    print('Olá Pequeno Gafanhoto você digitou {} e tem como Antecessor o valor de {} e Sucessor o valor de {} !'.format(n1, (n1-1), (n1+1)))


if __name__ == '__main__':
    main()
