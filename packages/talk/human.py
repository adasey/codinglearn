# from packages.tools import utils
from ..tools import utils # ..은 어느 위치에 있는지 알기 어렵기 때문에

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')