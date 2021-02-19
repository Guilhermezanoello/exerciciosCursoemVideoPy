"""
Programa que lê alturae largura de uma parede e diz quantos Litros de Tinta
é necessario para pintar. Cada Litrode tinta pinta 2m^2
"""


def main():
    lar = float(input('Digite a largura de sua parede: '))
    alt = float(input('Digite a altura de sua parde: '))
    area = lar * alt
    litro = area / 2
    print('Sua parede tem as dimensões de {}x{} e sua área é de {:.1f}m2.'.format(lar, alt, area))
    print('Para pintar sua parede, você precisará de {:.1f}litros de tinta.'.format(litro))


if __name__ == '__main__':
    main()