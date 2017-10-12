from pybot.nlp import classify

ACTIONS = {}


def register_action(class_name, method):
    """
    Register an action to be executed when the class be matched
    Args:
        class_name: The class name
        method:  A function to be executed
    """
    ACTIONS[class_name] = method


def _getaction(class_name):
    """ Returns an action based on the class name """
    if class_name in ACTIONS.keys():
        return ACTIONS[class_name]
    else:
        return None


def interact(frase):
    classification = classify(frase)
    action = _getaction(classification[0])
    response = action([frase])

    if response is None:
        raise ValueError('Action must return a response')

    return response
