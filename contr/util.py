import tensorflow as tf
import numpy as np


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

def pad_image(img, pad_t, pad_r, pad_b, pad_l):
    """Add padding of zeroes to an image.
    Add padding to an array image.
    :param img:
    :param pad_t:
    :param pad_r:
    :param pad_b:
    :param pad_l:
    """
    height, width = img.shape

    # Adding padding to the left side.
    pad_left = np.zeros((height, pad_l), dtype = np.int)
    img = np.concatenate((pad_left, img), axis = 1)

    # Adding padding to the top.
    pad_up = np.zeros((pad_t, pad_l + width))
    img = np.concatenate((pad_up, img), axis = 0)

    # Adding padding to the right.
    pad_right = np.zeros((height + pad_t, pad_r))
    img = np.concatenate((img, pad_right), axis = 1)

    # Adding padding to the bottom
    pad_bottom = np.zeros((pad_b, pad_l + width + pad_r))
    img = np.concatenate((img, pad_bottom), axis = 0)

    return img

def center_image(img):
    """Return a centered image.
    :param img:
    """
    col_sum = np.where(np.sum(img, axis=0) > 0)
    row_sum = np.where(np.sum(img, axis=1) > 0)
    y1, y2 = row_sum[0][0], row_sum[0][-1]
    x1, x2 = col_sum[0][0], col_sum[0][-1]

    cropped_image = img[y1:y2, x1:x2]

    zero_axis_fill = (img.shape[0] - cropped_image.shape[0])
    one_axis_fill = (img.shape[1] - cropped_image.shape[1])

    top = int(round(zero_axis_fill / 2))
    bottom = int(round(zero_axis_fill - top))
    left = int(round(one_axis_fill / 2))
    right = int(round(one_axis_fill - left))

    padded_image = pad_image(cropped_image, top, left, bottom, right)

    return padded_image
