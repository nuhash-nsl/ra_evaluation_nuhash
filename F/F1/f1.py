import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Sequential



TEST_VALUES = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def featurize(i):
    """featurize values

    Args:
        i (int): real value

    Returns:
        list : featurized list
    """
    return [1, i, i*i]
    
def generate_preprocess_data():
    """Create trainset and target set

    Returns:
        numpy_array: train set , target set
    """
    values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_train = np.array([5*i**2 + 7*i + 9 for i in values])
    x_train = np.array([featurize(i) for i in values])
    print(x_train.shape)
    print(y_train.shape)
    return x_train, y_train

def train_model(x_train, y_train):
    """Build and Train model

    Args:
        x_train (numpy array): trainset
        y_train (numpy array):  targetset

    Returns:
        Model : trained model
    """
    model = Sequential()
    model.add(Dense(50, input_shape=(3, ), activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=1000, batch_size=11)
    return model

def test_model(model):
    """Test the model

    Args:
        model (model): trained_model
    """
    for i in TEST_VALUES:
        print('If we input to our model : ', i, ', it should print: ', round(model.predict([featurize(i)])[0][0]))
        
if __name__ == "__main__":
    x, y = generate_preprocess_data()
    model = train_model(x,y)
    test_model(model)
    #print(y)
