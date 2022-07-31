import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import cv2

from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras import layers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Dropout, BatchNormalization, Input
from keras.callbacks import EarlyStopping
from keras import regularizers


from DataSet.create_dataset import *


def normalize_split_data(x, y):
    """Split dataset into train,test and validation.
       train test validation ratio is 60:20:20

    Args:
        x (numpy array): input image
        y (numpy array): target image

    Returns:
        numpy array: x_train, y_train, x_val, y_val, x_test, y_test
    """
    x = x.astype('float32') / 255.
    y = y.astype('float32') / 255.


    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

    x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.25, random_state=1)

    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    y_train = y_train.reshape((len(y_train), np.prod(y_train.shape[1:])))

    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
    y_test = y_test.reshape((len(y_test), np.prod(y_test.shape[1:])))

    x_val = x_val.reshape((len(x_test), np.prod(x_test.shape[1:])))
    y_val = y_val.reshape((len(y_test), np.prod(y_test.shape[1:])))



    return x_train, y_train, x_val, y_val, x_test, y_test


if __name__ == "__main__":

    generate_font_image()

    x, y = create_minst_dataset()

    syn_img_list = load_images_from_folder("./DataSet/Synthetic_Image")

    syn_img = generate_synthetic_image_dataset(y, syn_img_list)

    #visualize(10, x)
    #visualize(10, syn_img)

    x_train, y_train, x_val, y_val, x_test, y_test = normalize_split_data(x, syn_img)

    print(x_train.shape, y_train.shape, x_val.shape, y_val.shape, x_test.shape, y_test.shape)
    

    # visualize(10, x_train)
    # visualize(10, y_train)
    # visualize(10, x_val)
    # visualize(10, y_val)
    # visualize(10, x_test)
    # visualize(10, y_test)
