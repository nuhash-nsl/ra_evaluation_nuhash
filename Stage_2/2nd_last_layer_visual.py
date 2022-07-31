import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Dropout, BatchNormalization, Input
from keras.callbacks import EarlyStopping
from keras import regularizers

IMAGE_PATH = "./Inference_Image/sample_input/30.jpg"

from Model import model
from inference import load_best_model

if __name__ == "__main__":

    autoencoder = load_best_model()

    img = cv2.imread(IMAGE_PATH, 0)
    plt.imshow(img)
    plt.show()
    reshaped_img = img.reshape(1,784)
    predicted_img = autoencoder.predict(reshaped_img)

    model_layers = [ layer.name for layer in autoencoder.layers]
    print('layer name : ',model_layers)

    second_last_layer = Model(inputs=autoencoder.input, outputs=autoencoder.get_layer('conv2d_4').output)

    second_last_layer_features = second_last_layer.predict(reshaped_img)

    print('2nd last layer feature output shape:', second_last_layer_features.shape)

    plt.imshow(second_last_layer_features[0, :, :, 0])
    plt.show()
