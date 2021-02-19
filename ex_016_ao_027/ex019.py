"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice


def main():
    aluno1 = str(input('Digite o primeiro nome de aluno: '))
    aluno2 = str(input('Digite o segundo nome de aluno: '))
    aluno3 = str(input('Digite o terceiro nome de aluno: '))
    aluno4 = str(input('Digite o quarto nome de aluno: '))
    lista = [aluno1, aluno2, aluno3, aluno4]
    escolido = choice(lista)
    print('O aluno escolido foi {} ! Parabéns!!!'.format(escolido))


if __name__ == '__main__':
    main()
