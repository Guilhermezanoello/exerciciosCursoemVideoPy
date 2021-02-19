def main():
    algo = input('Digite algo: ')
    print('O tipo primitivo desse valor é {}'.format(type(algo)))
    print('Só tem espaços? {}'.format(algo.isspace()))
    print('É um número? {}'.format(algo.isnumeric()))
    print('É alfabético? {}'.format(algo.isalpha()))
    print('É alfanumérico? {}'.format(algo.isalnum()))
    print('Está em maiúculas? {}'.format(algo.isupper()))
    print('Está em minusculas ? {}'.format(algo.islower()))
    print('Está Capitalizada? {}'.format(algo.istitle()))


if __name__ == '__main__':
    main()