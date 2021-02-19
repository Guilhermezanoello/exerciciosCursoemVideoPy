"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""


def main():
    print('-=' * 15)
    print('Analisador de Triângulos!')
    print('-=' * 15)
    s1 = float(input('Digite a primeira medida: '))
    s2 = float(input('Digite a segunda medida: '))
    s3 = float(input('Digite a terceira medida: '))
    if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
        print('As medidas acima PODEM FORMAR um Triângulo!')
    else:
        print('As medidas acima NÃO PODEM FORMAR um Triângulo!')


if __name__ == '__main__':
    main()
