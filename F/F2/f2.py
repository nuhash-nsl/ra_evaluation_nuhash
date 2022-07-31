import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers
from keras.utils import plot_model



def create_data():

    """Generate Random Dataset
    Returns:
        tensors : train and test set 
    """

    X_train = np.random.rand(100, 35, 35, 3)
    y_train = np.random.rand(100,31, 31, 32)
    X_test = np.random.rand(100,35, 35, 3)
    y_test = np.random.rand(100,31, 31, 32)

    return X_train, y_train, X_test, y_test

def create_model():

    """Model Architechture Build
    Returns:
        Keras Model: Model 
    """

    inputsA=keras.layers.Input(shape=(35,35,3),)
    x=keras.layers.Conv2D(32, 3, name='conv_x')(inputsA)
    x=keras.layers.Activation('relu',name="relu_x")(x)


    inputsB=keras.layers.Input(shape=(35,35,3))
    y=keras.layers.Conv2D(32,3,name='conv_y')(inputsB)
    y=keras.layers.Activation('relu',name="relu_y")(y)

    # add x and y 
    z=keras.layers.Add()([x,y])
    z=keras.layers.Conv2D(32,3, name='conv_z')(z)
    z=keras.layers.Activation('relu',name="relu_z")(z)
    
    model=keras.Model(inputs=[inputsA, inputsB], outputs=z)
    model.summary()
    model.compile(optimizer='adam',loss='mse')
    plot_model(model, to_file='model.png')

    return model




if __name__ == "__main__":


    X_train, y_train, X_test, y_test = create_data()

    model = create_model()

    history = model.fit([X_train, X_train], y_train, epochs=100)

    results = model.evaluate([X_test, X_test], y_test)
    
    print("loss:",results)