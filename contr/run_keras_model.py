from keras.models import load_model
from keras.models import model_from_json
import keras
import numpy as np
from PIL import Image
import util

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded Model from disk")
loaded_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
# summary = loaded_model.summary()
img = np.invert(Image.open('img/img3.png').convert('L')).ravel().reshape(28, 28)
img_centered_to_feed = util.center_image(img)

img_centered_to_save = np.asarray(img_centered_to_feed, dtype=np.int8)
i = Image.fromarray(img_centered_to_save, 'L')
i.save('img/img3_c.png')

img_centered_to_feed = img_centered_to_feed.reshape(1, 28, 28, 1)
predicted_number = np.argmax(loaded_model.predict(img_centered_to_feed)[0])
print('Predicted number: ', predicted_number)

