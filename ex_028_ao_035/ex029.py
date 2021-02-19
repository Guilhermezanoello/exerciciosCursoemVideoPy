"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""


def main():
    veloz = float(input('Qual velocidade de um carro? '))
    if veloz > 80:
        multa = (veloz - 80)*7
        print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h')
        print('Você deve pagar uma multa de {:.2f} €'.format(multa))
    print('Tenha um bom dia! Digija com segurança!')


if __name__ == '__main__':
    main()
