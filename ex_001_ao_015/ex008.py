# Programa que lê metro e exibe em centimetro e milimetros

def main():
    m = float(input('Digite a distancia em metros: '))
    km = m * 0.001
    hm = m * 0.01
    dam = m * 0.1
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    print('A distancia de {}m é equivalente nas seguintes medidas: '.format(m))
    print('-'*13)
    print('Em {}km;\nEm {}hm;\nEm {}dam.'.format(km, hm, dam))
    print('Em {}dm;\nEm {}cm;\nEm {}mm.'.format(dm, cm, mm))
    print('-' * 13)


if __name__ == '__main__':
    main()