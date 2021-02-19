"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""


def main():
    salatual = float(input('Qual é o salário do funcionário: € '))
    if salatual <= 1250:
        novosal = (salatual * 0.15) + salatual
    else:
        novosal = (salatual * 0.10) + salatual
    print('Quem ganhava {:.2f} € passa a ganhar {:.2f} € agora!'.format(salatual, novosal))


if __name__ == '__main__':
    main()
