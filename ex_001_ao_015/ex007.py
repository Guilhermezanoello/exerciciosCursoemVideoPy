#Calcule a nota de dois alunos e mostre sua média:


def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2)/2
    print('A sua média é {:.1f} !!!'.format(media))


if __name__ == '__main__':
        main()
