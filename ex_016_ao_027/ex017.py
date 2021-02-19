"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""

#   catO = float(input('Qual o cumprimento do Cateto Oposto: '))
#   catA = float(input('Qual o cumprimento do Cateto Adjacente: '))
#   hipo = (catO ** 2 + catA ** 2) ** (1 / 2)
#   print('A Hipotenusa vai medir {:.2f}!'.format(hipo))

from math import hypot


def main():
    catO = float(input('Qual o cumprimento do Cateto Oposto: '))
    catA = float(input('Qual o cumprimento do Cateto Adjacente: '))
    hipo = hypot(catO, catA)
    print('A hipotenusa vai medir {:.2f}!'.format(hipo))


if __name__ == '__main__':
    main()
