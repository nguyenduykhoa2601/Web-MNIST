import tensorflow as tf
import numpy as np


class TensorflowModel:

    def __init__(self, model_h5_path):
        self._model_h5_path = model_h5_path
        self.model = self._load_model(self._model_h5_path)

    def _load_model(self, model_h5_path):
        return tf.keras.models.load_model(model_h5_path)

    def predict(self, data):
        prediction = self.model.predict(data)[0]

        return np.argmax(prediction)