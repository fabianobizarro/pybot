import sys
sys.path.append('../')
import pybot as bot


def cumprimento(*params):
    return "estou bem e você?"


def saudacao(*params):
    return "olá"


def initialize():
    bot.train('./data.json')

    bot.register_action('saudacao', saudacao)
    bot.register_action('cumprimento', cumprimento)


if __name__ == '__main__':
    initialize()
    frase = ' '.join(sys.argv[1:])
    r = bot.interact(frase)
    print(r)
