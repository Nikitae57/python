from model import Model
from train import train
import tensorflow as tf


def save_model():
    model = Model()
    train(model)
    with model.sess as sess:
        frozen_graph = tf.graph_util.convert_variables_to_constants(
            sess, sess.graph_def, ['output']
        )
        saver = tf.train.Saver()
        saver.save(sess, 'ckpt/model.ckpt')
    # with tf.gfile.GFile('model_pb/model.pb', "wb") as f:
    #     f.write(frozen_graph.SerializeToString())


if __name__ == '__main__':
    save_model()
