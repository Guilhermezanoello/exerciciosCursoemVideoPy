"""
Programa que lê um número e inteiro e mostra sua Tabuada
"""


def main():
    n = int(input('Digite um número e veja sua Tabuada!!! '))
    print('-' * 13)
    print('{} X {} = {}'.format(n, 1, n * 1))
    print('{} X {} = {}'.format(n, 2, n * 2))
    print('{} X {} = {}'.format(n, 3, n * 3))
    print('{} X {} = {}'.format(n, 4, n * 4))
    print('{} X {} = {}'.format(n, 5, n * 5))
    print('{} X {} = {}'.format(n, 6, n * 6))
    print('{} X {} = {}'.format(n, 7, n * 7))
    print('{} X {} = {}'.format(n, 8, n * 8))
    print('{} X {} = {}'.format(n, 9, n * 9))
    print('{} X {} = {}'.format(n, 10, n * 10))
    print('-' * 13)


if __name__ == '__main__':
    main()
