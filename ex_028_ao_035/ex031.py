"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""


def main():
    distancia = float(input('Qual a distância da sua viagem? '))
    print('Você está preste a começar uma viagem de {:.2f}Km'.format(distancia))
    if distancia <= 200:
        valor = distancia * 0.50

    else:
        valor = distancia * 0.45
    print('E o preço de sua viagem será de {:.2f}€!'.format(valor))


if __name__ == '__main__':
    main()
