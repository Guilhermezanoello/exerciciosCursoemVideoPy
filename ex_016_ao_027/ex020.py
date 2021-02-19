"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle


def main():
    aluno1 = str(input('Digite o primeiro nome de aluno: '))
    aluno2 = str(input('Digite o segundo nome de aluno: '))
    aluno3 = str(input('Digite o terceiro nome de aluno: '))
    aluno4 = str(input('Digite o quarto nome de aluno: '))
    lista = [aluno1, aluno2, aluno3, aluno4]
    shuffle(lista)
    print('A ordem da apresentação será :\n{}'.format(lista))


if __name__ == '__main__':
    main()