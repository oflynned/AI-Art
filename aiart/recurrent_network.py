import tensorflow as tf
from tensorflow.python.ops import rnn, rnn_cell
import numpy as np
from aiart.DataGenerator import *
from aiart.ColorMapping import *

# Network Parameters
n_input = 28 # MNIST data input (img shape: 28*28)
n_steps = 28 # timesteps
n_hidden = 128 # hidden layer num of features
n_classes = 10 # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_steps, n_input])
y = tf.placeholder("float", [None, n_classes])

# Define weights
weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, n_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([n_classes]))
}

def RNN(x, weights, biases):

    # Prepare data shape to match `rnn` function requirements
    # Current data input shape: (batch_size, n_steps, n_input)
    # Required shape: 'n_steps' tensors list of shape (batch_size, n_input)

    # Permuting batch_size and n_steps
    x = tf.transpose(x, [1, 0, 2])
    # Reshaping to (n_steps*batch_size, n_input)
    x = tf.reshape(x, [-1, n_input])
    # Split to get a list of 'n_steps' tensors of shape (batch_size, n_input)
    x = tf.split(0, n_steps, x)

    # Define a lstm cell with tensorflow
    lstm_cell = rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)

    # Get lstm cell output
    outputs, states = rnn.rnn(lstm_cell, x, dtype=tf.float32)

    # Linear activation, using rnn inner loop last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

# Initializing the variables
init = tf.initialize_all_variables()

d = DataGenerator()
d.generateData()
sensor_data = d.getSensorData()
dv = tf.placeholder(tf.float32, None)
temp = tf.reshape(dv, [1, n_input])
# temp = dv * 1
print(sensor_data[0][0:28])
with tf.Session() as s:
    s.run(init)
    for dt in range(len(sensor_data)):
        n = s.run(temp, feed_dict={dv: sensor_data[dt][0:28]})
        # out = s.run(RNN(n, weights, biases))
        out = s.run(RNN(n, weights, biases))
        # val = int(out)
        # print(ColorMapping.color_map(val))