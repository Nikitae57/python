import util
import tensorflow as tf
import numpy as np
from PIL import Image
import hparams as hp
from model import Model


def run_model(img_paths):
    model = Model()

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(session, 'ckpt/model.ckpt')

        output = tf.get_default_graph().get_tensor_by_name('output/BiasAdd:0')
        for img_path in img_paths:
            img = np.invert(Image.open(img_path).convert('L')).ravel()
            feed_dict = {model.X: [img], model.keep_prob: hp.dropout}
            prediction = session.run(tf.argmax(output, 1), feed_dict)
            print('Prediction for image {}:'.format(img_path),
                  np.squeeze(prediction))


if __name__ == '__main__':
    # graph_path = 'model_pb/model.pb'
    imgs = ['img/img2.jpg']
    run_model(imgs)
