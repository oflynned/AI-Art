# from numpy import exp, array, random, dot
import numpy as np
import tensorflow as tf
from aiart.DataGenerator import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import matplotlib.cm as cm

# shape = (50, 50)
# initial_board = tf.random_uniform(shape, minval=0, maxval=2, dtype=tf.int32)
# board = tf.placeholder(tf.int32, shape=shape, name='board')

# def update_board(X):
#     N = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
#     # Apply rules of the game
#     X = (N == 3) | (X & (N == 2))
#     return X
# board_update = tf.py_func(update_board, [board], [tf.int32])
# fig = plt.figure()


# Network Parameters

X = tf.placeholder("float", None)
# Store layers weight & bias
weights = {
    'encoder_h1' : tf.Variable(tf.random_normal([1, 100])),
}
biases = {
    'encoder_b1' : tf.Variable(tf.random_normal([100, 1])),
}

# Create model
def encoder(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']), biases['encoder_b1']))
    layer_1 = tf.nn.relu(layer_1)

    return layer_1

if __name__ == '__main__':
    # generate mock sensor input data
    dg = DataGenerator(100, 10)
    dg.generateData()
    data = np.asarray(dg.getSensorData())
    # print(data)
    # initialize variables for neural network implementation
    d = tf.placeholder('float32', None)
    y = tf.reshape(d, [100, 1])
    x = tf.placeholder('float32', None)
    fig = plt.figure()

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        for dt in range(len(data)):
            X = sess.run(y, feed_dict={d: data[dt]})
            out = sess.run(encoder(X))
            plot = plt.imshow(out, cmap='magma', interpolation='nearest')
            plt.show()
            plt.close()