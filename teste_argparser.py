import argparse

parser = argparse.ArgumentParser(description='Calcular a área')

parser.add_argument('-l', '--largura', type=float, help='Largura')
parser.add_argument('-c', '--comprimento', type=float, help='Comprimento')

args = parser.parse_args()


def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area


if __name__ == '__main__':
    print(f'O valor da área é {calcula_area(args.largura, args.comprimento)}')
