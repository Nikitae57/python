from keras.models import load_model
from keras.models import model_from_json
import keras
import numpy as np
from PIL import Image
from numpy.core._multiarray_umath import ndarray

import util


class Inference:
    def __init__(self):
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights("model.h5")
        print("Loaded Model from disk")
        self.loaded_model.compile(loss=keras.losses.categorical_crossentropy,
                                  optimizer=keras.optimizers.Adadelta(),
                                  metrics=['accuracy'])

    def predict(self, img_path) -> int:
        # Image.fromarray()
        img = Image.open(img_path).convert('L')
        img.thumbnail((28, 28), Image.ANTIALIAS)
        img = np.invert(img).reshape(28, 28)
        img_centered_to_feed = util.center_image(img)

        img_centered_to_save = np.asarray(img_centered_to_feed, dtype=np.int8)
        i = Image.fromarray(img_centered_to_save, 'L')
        i.save('img/processed_img.png')

        img_centered_to_feed = img_centered_to_feed.reshape(1, 28, 28, 1)
        predicted_number = np.argmax(self.loaded_model.predict(img_centered_to_feed)[0])

        return predicted_number
