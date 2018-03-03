import sys
sys.path.append('../')

from nltk.stem import RSLPStemmer
from pybot import PyBot

def cumprimento(*params):
    return "estou bem e você?"


def saudacao(*params):
    return "olá"


bot = PyBot()
bot.set_stemmer(RSLPStemmer())

bot.train('./data.json')


bot.register_action('saudacao', saudacao)
bot.register_action('cumprimento', cumprimento)
#
print(bot.interact('oi'))
print(bot.interact('tudo bem?'))