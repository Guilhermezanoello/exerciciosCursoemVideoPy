"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint  # Importa uma função de escolha aleatória
from time import sleep  # Importa uma função temporiza


def main():
    computador = randint(0, 5)  # Faz o computador "PENSAR"
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print('-=-' * 20)
    jogador = int(input('Em que número eu pensei? '))  # O Jogador tenta adivinhar o número.
    print('PROCESSANDO...')
    sleep(3)  # Temporiza em 3 seg
    if jogador == computador:  # Testa se os números são iguais
        print('Parabéns! Você conseguir me Vencer!')
    else:
        print('GANHEI! Eu pensei no número {} e não no número {}! TENTE OUTRA VEZ!'.format(computador, jogador))


if __name__ == '__main__':
    main()
