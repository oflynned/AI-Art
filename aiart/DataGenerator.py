import random

MIN_SENSOR_VALUE = 0
MAX_SENSOR_VALUE = 255

class DataGenerator(object):
    def __init__(self, number_of_sensors, number_of_entries):
        self.number_of_sensors = number_of_sensors
        self.number_of_sensor_entries = number_of_entries
        self.data = []

    def generateData(self):
        sensor_data = []
        # loop through the number of sensor inputs required
        for x in range(self.number_of_sensor_entries):
            # loop through the number of sensor entries for each sensor
            for entry in range(self.number_of_sensors):
                sensor_data.append(random.randint(MIN_SENSOR_VALUE, MAX_SENSOR_VALUE))
            self.data.append(list(sensor_data))
            sensor_data.clear()

    def getSensorData(self):
        return self.data