import sys
sys.path.append('../')


import pybot as bot


def cumprimento(*params):
    return "estou bem e você?"


def saudacao(*params):
    return "olá"


bot.train('./data.json')

bot.register_action('saudacao', saudacao)
bot.register_action('cumprimento', cumprimento)

print(bot.interact('oi'))
print(bot.interact('tudo bem?'))