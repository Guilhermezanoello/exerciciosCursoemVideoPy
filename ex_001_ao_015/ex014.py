"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""


def main():
    tem = float(input('Informe qual a temperatura em ºC: '))
    fai = tem * 1.8 + 32
    print('A temperatura de {}ºC corresponde a {:.1f}ºF!'.format(tem, fai))


if __name__ == '__main__':
    main()
