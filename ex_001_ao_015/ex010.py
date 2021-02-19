"""
Programa que lê o Valor em que uma pessoa tem e mostra quantos reais ela pode comprar ganhando em EURO
"""


def main():
    money = float(input('Digite quantos Euros(€) você tem em suas carteira(use somente números separando os com ponto):'))
    real = 6.39
    print('Você tem {:.2f} € e com isso dá para comprar R$ {:.2f} .'.format(money, money * real))


if __name__ == '__main__':
    main()