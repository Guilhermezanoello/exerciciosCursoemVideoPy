"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint  # Importa uma função de escolha aleatória
from time import sleep  # Importa uma função temporiza


def main():
    cores = {'limpa': '\033[m', 'Azulclaro': '\033[1;36m',  # Lista de Cores
             'Verdeclarosub': '\033[4;1;32m', 'Branco': '\033[1m',  # Padrão ANSI ESCAPE SEQUENCE
             'Vermelho': '\033[1;31m', 'Amarelo': '\033[1;33m',
             'Lilas': '\033[1;35m'}
    computador = randint(0, 5)  # Faz o computador "PENSAR"
    print('{}-=-{}'.format(cores['Azulclaro'], cores['limpa']) * 20)
    print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores['Verdeclarosub'], cores['limpa']))
    print('{}-=-{}'.format(cores['Azulclaro'], cores['limpa']) * 20)
    jogador = int(input('{}Em que número eu pensei?{} '.format(cores['Branco'],
                                                               cores['limpa'])))  # O Jogador tenta adivinhar o número.
    print('{}PROCESSANDO...{}'.format(cores['Vermelho'], cores['limpa']))
    sleep(3)  # Temporiza em 3 seg
    if jogador == computador:  # Testa se os números são iguais
        print('{}Parabéns! Você conseguir me Vencer!{}'.format(cores['Amarelo'], cores['limpa']))
    else:
        print('{}GANHEI! Eu pensei no número {} e não no número {}!\nTENTE OUTRA VEZ!{}'.format(cores['Lilas'],
                                                                                                computador, jogador,
                                                                                                cores['limpa']))


if __name__ == '__main__':
    main()
