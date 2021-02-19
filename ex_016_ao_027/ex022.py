"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:

    – O nome com todas as letras maiúsculas e minúsculas.

    – Quantas letras ao todo (sem considerar espaços).

    – Quantas letras tem o primeiro nome.
"""


def main():
    name = str(input('Digite seu nome completo: ')).strip()  # retira os espaço do inicio e fim.
    print('Analisando seu nome temos...')
    print('Seu nome em maiúsculas é {}.'.format(name.upper()))
    print('Seu nome em minúsculas é {}.'.format(name.lower()))
    print('Seu nome tem ao todo {} letras.'.format(len(name) - name.count(' ')))
    sepname = name.split()  # fatia a string
    print('Seu primeiro nome é {} e ele tem {} letras.'.format(sepname[0], len(sepname[0])))


if __name__ == '__main__':
    main()
