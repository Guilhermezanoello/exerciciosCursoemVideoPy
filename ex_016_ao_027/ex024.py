"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""


def main():
    city = str(input('Em que cidade você nasceu: ')).strip()
    print(city[:5].upper() == 'SANTO')


if __name__ == '__main__':
    main()
