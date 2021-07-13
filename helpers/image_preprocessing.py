from enum import auto
import numpy as np
from PIL import Image
from io import BytesIO
from base64 import b64decode
import  sklearn.svm  
class ImageProcessor:

    def __init__(self, image_url):
        self.image_url = image_url

    def _decode_image(self, image_url):
        _, encoded = image_url.split(',')

        return BytesIO(b64decode(encoded))

    def _reshape_image(self, image_bytes): 
        image = Image.open(image_bytes)

        return image.resize((28,28),Image.LANCZOS)

    def prepare_image_for_evaluation(self):
        decoded_image = self._decode_image(self.image_url)
        reshaped_image = self._reshape_image(decoded_image)
        image_array = np.array(reshaped_image)[:, : ,3]/255
        
        return image_array.reshape(-1,28,28,1)