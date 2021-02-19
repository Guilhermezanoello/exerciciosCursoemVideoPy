"""Mostrar o Dobro o Triplo e a Raiz Quadrada de um número"""


def main():
    num = int(input('Digite um número aqui : '))
    print('O Dobro de {} é {} !!\nO Triplo de {} é {}!!!\nA Raiz Quadrada de {} é {:.2f} !'.format(num, num*2, num, num*3, num, num**(1/2)))


if __name__ == '__main__':
    main()