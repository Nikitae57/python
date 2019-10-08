from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import hparams as hp
from model import Model


def train(model):
    mnist = input_data.read_data_sets('mnist_data', one_hot=True)
    n_train = mnist.train.num_examples
    n_validation = mnist.validation.num_examples
    n_test = mnist.test.num_examples

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()

        # for i in range(hp.n_iterations):
        i = 0
        minibatch_loss = 1.0
        minibatch_accuracy = 0
        while minibatch_accuracy <= 0.99 and minibatch_loss >= 0.15:
            batch_x, batch_y = mnist.train.next_batch(hp.batch_size)
            sess.run(model.train_step, feed_dict={
                model.X: batch_x, model.Y: batch_y, model.keep_prob: hp.dropout
            })

            # print loss and accuracy (per minibatch)
            if i % 100 == 0:
                minibatch_loss, minibatch_accuracy = sess.run(
                    [model.cross_entropy, model.accuracy],
                    feed_dict={model.X: batch_x, model.Y: batch_y, model.keep_prob: 1.0}
                )
                print(
                    "Iteration",
                    str(i),
                    "\t| Loss =",
                    str(minibatch_loss),
                    "\t| Accuracy =",
                    str(minibatch_accuracy)
                )
            i += 1

        saver.save(sess, 'ckpt/model.ckpt')


if __name__ == '__main__':
    model = Model()
    train(model)
