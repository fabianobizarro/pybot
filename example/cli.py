import sys
sys.path.append('../')
from pybot import PyBot
from nltk.stem import RSLPStemmer


def cumprimento(*params):
    return "estou bem e você?"


def saudacao(*params):
    return "olá"


def initialize(bot: PyBot):
    bot.train('./data.json')
    bot.register_action('saudacao', saudacao)
    bot.register_action('cumprimento', cumprimento)


if __name__ == '__main__':
    bot = PyBot(RSLPStemmer())
    initialize(bot)
    sentence = ' '.join(sys.argv[1:])
    r = bot.interact(sentence)
    print(r)
