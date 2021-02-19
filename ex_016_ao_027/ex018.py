"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan


def main():
    angulo = int(input('Digite o ângulo que tu desejas: '))
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    print('O ângulo: {},tem SENO: {:.2f},COSSENO: {:.2f} e TANGENTE: {:.2f} !'.format(angulo,seno,cosseno,tangente))


if __name__ == '__main__':
    main()
