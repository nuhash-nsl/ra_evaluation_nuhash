import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import cv2
from tensorflow import keras
from keras.datasets import mnist
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def generate_font_image():
    """
    Generates 0-9 synthetic images with time roman font and saves in a directory
    """
    for i in range(10):
        img = Image.new('RGB', (28,28), (0,0,0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./DataSet/Font/times-roman.ttf", 35)
        draw.text((6, -3),str(i),(255,255,255),font=font)
        #resized_img = img.resize((round(28), round(28)))
        thresh = 30
        fn = lambda x : 255 if x > thresh else 0
        img = img.convert('L').point(fn, mode='1')
        img.save('./DataSet/Synthetic_Image/'+str(i)+'.jpg')

def load_images_from_folder(folder):
    """Loads 10 synthetic image from directory in sorted order.

    Args:
        folder (String): File path to synthetic image

    Returns:
        list: list of synthetic image in sorted order
    """

    images = []
    #print(len(images))
    for filename in sorted(os.listdir(folder)):
        #print(filename[:1])
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
             images.append(img)
    return images



def visualize(n, image_array):
    """Visualize images with required number

    Args:
        n (int): number of images user want to see
        image_array (numpy array): numpy array of images
    """     
    # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(image_array[int(i)].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()




def create_minst_dataset():
    """Creates mnist dataset,concates train and test set with label

    Returns:
        numpy array: images array, label of images
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #print(x_train.shape)
    x = np.concatenate((x_train,x_test), axis= 0)
    #print(x.shape)
    y = np.concatenate((y_train, y_test), axis = 0)
    #y = np.reshape(y,(-1,1))
    #print(y.shape)
    return x, y

def generate_synthetic_image_dataset(label_list , syn_image_list):
    """Generates Synthetic images dataset with mnist label

    Args:
        label_list (list): label list from minst
        syn_image_list (numpy array): synthetic image list(0-9)

    Returns:
        image list: synthetic image dataset made with mnist labels.
    """
    syn_img_list = []
    for i in label_list:
        
        syn_img_list.append(syn_image_list[i])

    syn_img_numpy =  np.array(syn_img_list)
    return syn_img_numpy



if __name__ == "__main__":
    
    generate_font_image()

    x, y = create_minst_dataset()

    syn_img_list = load_images_from_folder("./DataSet/Synthetic_Image")

    syn_img = generate_synthetic_image_dataset(y, syn_img_list)

    #print(syn_img.shape)
    visualize(10, x)
    visualize(10, syn_img)




