import random

class ColorMapping(object):
    WARM = 30
    MILD = 20
    COLD = 10

    def __init__(self):
        pass

    @staticmethod
    def color_map(x):
        if x < ColorMapping.COLD:
            output = (0, 0, random.randint(0, 255))
        elif x < ColorMapping.MILD:
            output = (85, 85, 85)
        else:
            output = (random.randint(0, 255), 0, 0)
        return output