from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros, [784, 10])
b = tf.Variable(tf.zeros, [10])

# predict
y = tf.nn.softmax(tf.matmul(x, W) + b)

# acutal
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = - tf.reduce_sum(y_ * tf.log(y))

# training
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# init
init = tf.initialize_all_variables()

# run
sess = tf.Session()
sess.run(init)
