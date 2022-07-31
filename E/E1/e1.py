import numpy as np
import PIL
from PIL import ImageOps
from PIL import Image

def read_image():
    """Read image

    Returns:
        numpy_array: image
    """

    #read_image
    image_file = PIL.Image.open("./image-segmentation.JPG")
    image_file = ImageOps.grayscale(image_file) 
    image_array = np.array(image_file)


    #inverse_image
    image_array = 255 - image_array
    return image_array

def threshold(image_array, thresh):
    """Apply thresholding on image

    Args:
        image_array (numpy array): input image
        thresh (int): thresholding value

    Returns:
        numpy array: thresholded image
    """
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            if (image_array[i,j]) < 60:
                image_array[i,j] = 0
            else:
                image_array[i,j] = 255
    return image_array



def row_wise_crop(image_array):
    """crop image in lines row wise

    Args:
        image_array (numpy_array): image

    Returns:
        int: number of rows cropped
    """
    row_sum = np.sum(image_array, axis=1)

    row_number = 0
    checker = 0
    for i in range(image_array.shape[0]):
        if checker == i:
            checker += 1
            if row_sum[i] != 0:
                for j in range(i,image_array.shape[0]):
                    if row_sum[j] == 0:
                        new_img = image_array[i:j, :]
                        checker = j
                        image = Image.fromarray(new_img)
                        image.save( "./Row_Image/"+ 'img' + str(row_number) + '.png')
                        row_number += 1
                        break
                    
    return row_number
        

def col_wise_crop(row_number):
    """column wise crop on image,segments charachter in line

    Args:
        row_number (int): number of rows to cut on image
    """
    for number in range(0,row_number):
        image_file = PIL.Image.open("./Row_Image/"+ "img" +str(number) + ".png")
        image_array = np.array(image_file)
    
        col_number = 0
        checker2 = 0
        col_sum = np.sum(image_array , axis = 0)
        for i in range(image_array.shape[1]):
            if checker2 == i:
                #print("value of i", i)
                checker2 += 1
                if col_sum[i] != 0:
                    for j in range(i,image_array.shape[1]):
                        #print("value of j", j)
                        if col_sum[j] == 0:
                            new_img = image_array[:, i:j]
                            checker2 = j
                            image = Image.fromarray(new_img)
                            image.save('./Col_Image/'+ 'img' + str(number) + "_" + str(col_number) + '.png')
                            #print("image saved")
                            col_number += 1
                            break
    
          
    
if __name__ == "__main__":
    image_array = read_image()
    image_array = threshold(image_array, 60)
    row_number = row_wise_crop(image_array)
    #print(row_number)
    col_wise_crop(row_number)
    
