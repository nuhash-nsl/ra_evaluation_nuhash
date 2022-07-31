import matplotlib.pyplot as plt
import zipfile
import os
import cv2

from datetime import datetime
from packaging import version

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from tensorflow import keras
from keras import layers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Dropout, BatchNormalization, Input
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint

from DataSet.create_dataset import *
from utils import normalize_split_data
from Model.model import model


if __name__ == "__main__":

    generate_font_image()

    x, y = create_minst_dataset()

    syn_img_list = load_images_from_folder("./DataSet/Synthetic_Image")

    syn_img = generate_synthetic_image_dataset(y, syn_img_list)

    #visualize(10, x)
    #visualize(10, syn_img)

    x_train, y_train, x_val, y_val, x_test, y_test = normalize_split_data(x, syn_img)
    print(x_train.shape, y_train.shape, x_val.shape, y_val.shape, x_test.shape, y_test.shape)

    autoencoder = model()

    logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)
    checkpoint = ModelCheckpoint("./Model/best_model.h5", 
    verbose=1, 
    monitor='val_loss',
    save_best_only=True, 
    mode='min')

    autoencoder.fit(x_train, y_train,
                epochs=20,
                batch_size=24,
                shuffle=True,
                validation_data=(x_val, y_val),
                callbacks=[tensorboard_callback, checkpoint])


    decoded_imgs = autoencoder.predict(x_test)

    #print(decoded_imgs.shape)
    #print(type(decoded_imgs))
    #print(decoded_imgs[0])
    #print(decoded_imgs[0].shape)
    
    visualize(10,x_test)
    visualize(10,decoded_imgs)

    #tensorboard --logdir /home/nsl48/Desktop/ra_evaluation_nuhash/Stage_2/logs/scalars
