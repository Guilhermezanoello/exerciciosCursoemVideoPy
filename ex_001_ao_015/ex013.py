#Um Programa que leia o salário de um funcionário com um aumento de 15%

def main():
    sal = float(input('Qual o salário do funcionário(use números ): '))
    print('Um funcinário que ganhava {}€, com 15% de aumento, passa a receber {:.2f}€.'.format(sal, sal + (sal*0.15)))


if __name__ == '__main__':
    main()