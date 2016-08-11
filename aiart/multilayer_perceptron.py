import tensorflow as tf
from aiart.DataGenerator import *
from aiart.ColorMapping import *
from aiart.Screen import *
# from DataGenerator import *
# from ColorMapping import *
# from Screen import *
import numpy as np

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 256 # 2nd layer number of features
n_input = 256
n_classes = 5 # total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.sigmoid(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Initializing the variables
init = tf.initialize_all_variables()

# d = DataGenerator()
screen = Screen()
# d.generateData()
# sensor_data = d.getSensorData()
sensor_data = []
data = open('data.csv', 'r').readlines()
for line in data:
    temp = []
    splitted = line.split(',')
    for elem in splitted:
        temp.append(int(elem))
    sensor_data.append(list(temp))

dv = tf.placeholder(tf.float32, None)
temp = tf.reshape(dv, [1, n_input])
with tf.Session() as s:
    s.run(init)
    for dt in range(len(sensor_data)):
        # print(sensor_data[dt])
        n = s.run(temp, feed_dict={dv: sensor_data[dt]})
        out = s.run(multilayer_perceptron(n, weights, biases))
        X = int(out[0][0] % screen.WIDTH)
        Y = int(out[0][1] % screen.HEIGHT)
        R = int(out[0][2] % 255)
        G = int(out[0][3] % 255)
        B = int(out[0][4] % 255)
        print(X, Y, R, G, B)
        color = (R, G, B)
        screen.draw(X, Y, color)
