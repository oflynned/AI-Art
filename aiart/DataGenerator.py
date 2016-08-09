import random

MIN_SENSOR_VALUE = 0
MAX_SENSOR_VALUE = 30
SENSOR_ENTRIES = 1000
DATA_VECTOR_LENGTH = 784

class DataGenerator(object):
    def __init__(self):
        self.data = []

    def generateData(self):
        for entry in range(SENSOR_ENTRIES):
            d = []
            for vec in range(DATA_VECTOR_LENGTH):
                d.append(random.randint(MIN_SENSOR_VALUE, MAX_SENSOR_VALUE))
            self.data.append(list(d))

    def getSensorData(self):
        return self.data


    def generateDataFile(self):
        pass