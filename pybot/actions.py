ACTIONS = {}

def register_action(class_name, method):
    """
    Register an action to be executed when the class be matched
    Args:
        name (str): The class name
        method (function): A funciton to be exectued 
    """
    ACTIONS[class_name] = method


def get_action(class_name):
    """ Returns an action based on the class name """
    if class_name in ACTIONS.keys():
        return ACTIONS[class_name]
    else:
        return None
