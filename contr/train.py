from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


def train():
    mnist = input_data.read_data_sets('train_data', one_hot=True)
    batch = 100
    learning_rate = 0.01
    training_epochs = 10

    input = tf.placeholder(tf.float32, [None, 784])  # 28x28 pixels images
    output = tf.placeholder(tf.float32, [None, 10])  # 10 digits

    weight = tf.Variable(tf.zeros([784, 10]))
    bias = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(input, weight) + bias)


if __name__ == '__main__':
    train()
