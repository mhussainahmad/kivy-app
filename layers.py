# Custom L1 Distance Layer module


# Importing Dependencies
import tensorflow as tf
from tensorflow.keras.layers import Layer


# Custom L1Dist Layer from jupyter
# Siamese L1 Distance class
class L1Dist(Layer):

    # Init method - inheritance
    def __init__(self, **kwargs):
        super().__init__()

    # Magic happens here - similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)
