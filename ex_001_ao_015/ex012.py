"""
Programa que lê o preço de um produto e mostra um novo valor com 5% de Desconto
Bonus: faça uma opção de pagamento com juros.
"""


def main():
    valor = float(input('Qual é o preço do produto(use somente números): '))
    desc = valor-(valor*0.05)
    aum = valor+((valor*0.05)*10)
    print('O produto que custa {}€, ao pagar em dinheiro, ganha 5% de desconto.'.format(valor))
    print('Pagando um preço final de {}€.'.format(desc))
    print('Ao pagar em 10 vezes tens um juros de 5% ao mês.\nPagando um preço final de {}€.'.format(aum))


if __name__ == '__main__':
    main()
