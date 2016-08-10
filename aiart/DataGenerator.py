import random
from enum import Enum
import numpy as np

MIN_SENSOR_VALUE = 0
MAX_SENSOR_VALUE = 30
SENSOR_ENTRIES = 1000
# DATA_VECTOR_LENGTH = 784
DATA_VECTOR_LENGTH = 256


class InputState(Enum):
    LOW = "low"
    MED = "med"
    HIGH = "high"


class DataGenerator(object):
    def __init__(self):
        self.data = []

    def generateData(self):
        for entry in range(SENSOR_ENTRIES):
            d = []
            for vec in range(DATA_VECTOR_LENGTH):
                d.append(random.randint(MIN_SENSOR_VALUE, MAX_SENSOR_VALUE))
            self.data.append(list(d))

    @staticmethod
    def generate_tiered_values(vectors_per_tier):
        d = np.empty([1,3])
        for i in range(0, vectors_per_tier):
            new_data = np.array(
                [[DataGenerator.generate_state_limit(InputState.LOW), DataGenerator.generate_state_limit(InputState.MED),
                 DataGenerator.generate_state_limit(InputState.HIGH)]])
            d = np.concatenate((d, new_data))
        return d

    def getSensorData(self):
        return self.data

    def generateDataFile(self):
        pass

    @staticmethod
    def generate_state_limit(tier):
        if tier == InputState.LOW:
            return random.randrange(0, 101)
        elif tier == InputState.MED:
            return random.randrange(100, 201)
        elif tier == InputState.HIGH:
            return random.randrange(200, 256)
