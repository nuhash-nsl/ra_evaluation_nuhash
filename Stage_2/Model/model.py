from tensorflow import keras
from keras import layers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Dropout, BatchNormalization, Input
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.callbacks import ModelCheckpoint

def model():
    """Creates the model

    Returns:
        model: designed model
    """
    
    
    input_img = keras.Input(shape=(784, ))
    
    x = layers.Reshape((28, 28,1))(input_img)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)

    x = layers.Flatten()(x)
    x = layers.Dense(1568, activation='relu')(x)
    x = layers.Dense(100, activation = 'relu')(x)
    x = layers.Dense(1568, activation = 'relu')(x)

    x = layers.Reshape((7, 7, 32))(x)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.UpSampling2D((2, 2))(x)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.UpSampling2D((2, 2))(x)
    x = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
    x = layers.Flatten()(x)
    x = layers.Dense(784, activation='sigmoid')(x)

    decoded = layers.Reshape((784, ))(x)


    adam = keras.optimizers.Adam(
        learning_rate=0.0001,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-07,
        amsgrad=False,
        name="Adam",
    )

    autoencoder = keras.Model(input_img, decoded)
    autoencoder.compile(optimizer=adam, loss='binary_crossentropy')

    autoencoder.summary()

    return autoencoder


if __name__ == "__main__":
    autoencoder = model()
