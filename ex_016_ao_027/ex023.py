"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""


def main():
    num = int(input('Informe um número: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('\nAnalizando o número {} temos:'.format(num))
    print('Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}.'.format(u, d, c, m))


if __name__ == '__main__':
    main()
