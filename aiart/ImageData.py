import numpy as np
from PIL import Image

class ImageData(object):
    def __init__(self):
        self.i = 0
        self.j = 0
        self.matrix = np.empty((100, 100), dtype=np.uint8)

    def createImage(self, row):
        data = []
        for r in row:
            # make sure that every element in the row has 9 digits
            r *= 1000000000
            data.append(self.separateDigits(int(r)))

        # np.append(self.matrix, tuple(data))
        print(len(data))

    def separateDigits(self, number):
        number_of_digits = 9
        temp_color = []
        for _ in range(number_of_digits):
            temp_color.append(str(int(number % 10)))
            number /= 10
        R = int(''.join(temp_color[0:3]))
        G = int(''.join(temp_color[3:6]))
        B = int(''.join(temp_color[6:9]))
        R %= 255
        G %= 255
        B %= 255
        color = (R, G, B)
        return tuple(color)

    def showImage(self):
        np.reshape(self.matrix, (100, 100))
        # print(self.matrix)
        # img = Image.frombuffer('RGBA', (100, 100), self.matrix.tostring())
        # print(img.getdata())
        # img.show()