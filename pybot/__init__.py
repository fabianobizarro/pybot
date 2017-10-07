"""
Pybot
Finish this documentation
"""
from .nlp import train, classify
from .actions import register_action, get_action

def interact(frase):
    classification = classify(frase)
    action = get_action(classification[0])
    response = action([frase])

    if response is None:
        raise ValueError('Action must return a respose')

    return response
