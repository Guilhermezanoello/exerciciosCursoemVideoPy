"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

# num = float(input('Insira uma número'))
# print('O valor digitado foi {} e sua parte inteira é  {}.'.format(num, int(num)))


from math import trunc


def main():
    num = float(input('Insira um número: '))
    print('O valor digitado foi {} e sua parte inteira é {}.'.format(num, trunc(num)))


if __name__ == '__main__':
    main()
