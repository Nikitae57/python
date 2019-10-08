import tensorflow as tf
import hparams as hp


class Model:
    def __init__(self):
        n_input = 784  # input layer (28x28 pixels)
        n_hidden1 = 512  # 1st hidden layer
        n_hidden2 = 256  # 2nd hidden layer
        n_hidden3 = 128  # 3rd hidden layer
        n_output = 10  # output layer (0-9 digits)

        self.X = tf.placeholder("float", [None, n_input], name='in')
        self.Y = tf.placeholder("float", [None, n_output])
        self.keep_prob = tf.placeholder(tf.float32)

        self._X = tf.reshape(self.X, shape=[-1, 28, 28, 1])
        self.conv1 = tf.layers.conv2d(self._X, 32, 5, activation=tf.nn.relu)
        self.conv1 = tf.layers.max_pooling2d(self.conv1, 2, 2)

        self.conv2 = tf.layers.conv2d(self.conv1, 64, 3, activation=tf.nn.relu)
        self.conv2 = tf.layers.max_pooling2d(self.conv2, 2, 2)

        self.fc1 = tf.layers.flatten(self.conv2)
        self.fc1 = tf.layers.dense(self.fc1, 1024)
        self.fc1 = tf.layers.dropout(self.fc1, rate=hp.dropout, training=True)

        self.output = tf.layers.dense(self.fc1, hp.n_output, name='output')
        # tf.identity(self.output, 'out')

        self.cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(
                labels=self.Y, logits=self.output
            ))
        self.train_step = tf.train.AdamOptimizer(hp.learning_rate).minimize(self.cross_entropy)
        self.correct_pred = tf.equal(tf.argmax(self.output, 1), tf.argmax(self.Y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_pred, tf.float32))
