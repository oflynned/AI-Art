import tensorflow as tf
from aiart.DataGenerator import *
from aiart.ColorMapping import *
from aiart.Screen import *

# Parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 256 # 2nd layer number of features
n_input = 784
n_classes = 1 # total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
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

d = DataGenerator()
screen = Screen()
d.generateData()
sensor_data = d.getSensorData()
dv = tf.placeholder(tf.float32, None)
temp = tf.reshape(dv, [1, n_input])
with tf.Session() as s:
    s.run(init)
    for dt in range(len(sensor_data)):
        n = s.run(temp, feed_dict={dv: sensor_data[dt]})
        out = s.run(multilayer_perceptron(n, weights, biases))
        val = int(out)
        color = ColorMapping.color_map(val)
        screen.draw(color)
        # print(screen.returnSurfaceArray())