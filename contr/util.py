import tensorflow as tf


def load_graph(ckpt_path='ckpt/model.ckpt'):
    n_input = 784
    n_output = 10

    with tf.Graph().as_default() as g:
        input = tf.placeholder("float", [None, n_input], 'input')
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess, ckpt_path)
        frozen_graph_def = tf.graph_util.convert_variables_to_constants(
            sess, sess.graph_def, ['output']
        )
        tf.train.init_from_checkpoint

    return sess
