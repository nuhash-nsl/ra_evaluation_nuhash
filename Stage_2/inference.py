from statistics import mode
from tensorflow import keras
from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
 
def load_best_model():

    """Load best trained model.

    Returns:
        model: best trained model
    """

    # load model
    model = load_model("./Model/best_model.h5")
    # load single data
    return model

def inference(image_path,model):
    
    """Takes input image with file path and saves the output in a output file.

    Args:
        image_path (String): input image file path
        model (model): best trained model
    """

    img = cv2.imread(image_path, 0)
    plt.imshow(img, cmap=cm.gray)
    plt.show()
    reshaped_img = img.reshape(1,784)
    predicted_img = model.predict(reshaped_img)
    output = predicted_img.reshape(28, 28)
    plt.imshow(output, cmap=cm.gray)
    plt.show()
    plt.imsave("./Inference_Image/sample_output/output.jpg", output, cmap=cm.gray)

if __name__ == "__main__":
    model = load_best_model()
    model.summary()
    #inferene image path
    path = "./Inference_Image/sample_input/30.jpg"
    inference(path,model)

