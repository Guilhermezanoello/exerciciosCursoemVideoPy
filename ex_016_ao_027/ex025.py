"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""


def main():
    name = str(input('Digite seu nome complete: ')).strip()
    print('Seu nome tem Silva? {}'.format('SILVA' in name.upper()))


if __name__ == '__main__':
    main()
