from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from model import Model
import numpy as np
from PIL import Image


def test():
    model = Model()
    mnist = input_data.read_data_sets('mnist_data', one_hot=True)

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(session, 'ckpt/model.ckpt')

        output = tf.get_default_graph().get_tensor_by_name('output/BiasAdd:0')

        # img = np.asarray(Image.open(img_path).convert('L')).ravel()
        # feed_dict = {model.X: [img], model.keep_prob: hp.dropout}
        # prediction = session.run(tf.argmax(output, 1), feed_dict)
        # print('Prediction for image {}:'.format(img_path),
        #       np.squeeze(prediction))

    # model = Model()
    # train(model)
    #
    # mnist = input_data.read_data_sets('mnist_data', one_hot=True)
    # test_accuracy = model.sess.run(model.accuracy,
    #                                feed_dict={model.X: mnist.test.images,
    #                                           model.Y: mnist.test.labels,
    #                                           model.keep_prob: 1.0})
    #
    # print("\nAccuracy on test set:", test_accuracy)


if __name__ == '__main__':
    test()