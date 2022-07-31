import requests
import os, os.path

from os.path import exists
from bs4 import *
from PIL import Image

  
# CREATE FOLDER
def folder_create(images,num):
    """Create folder 

    Args:
        images : images to be saved.
        num (int): number of images to be saved
    """
    #create folder name Images
    folder_name = ("./image")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    download_images(images, folder_name, num)
  
#Download Images
def download_images(images, folder_name, num):
    """Donload images and save in directory

    Args:
        images : images
        folder_name (string): name of the folder
        num (int): number of images to be downloaded
    """
    count = 0
    print(f"Total {len(images)} Image Found!")
    if num > len(images):
        print("We could not find " + str(num - len(images)) + " images")
        print(len(images))
    else:
            print("we have found all images")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass

            try:
                r = requests.get(image_link).content
                try:
  
                    r = str(r, 'utf-8')
  
                except UnicodeDecodeError:
  
                    with open(f"{folder_name}/images{i}.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass
  
        if count == len(images):
            print("All Images Downloaded!")
              
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


def resize_image():
    """
    Resizes the downloaded images and save in preprocessed folder
    """
    imgs = []
    path = "./image"
    valid_images = [".jpg", ".gif", ".png", ".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path,f)))
    i = 1
    for img in imgs:
        new_img = img.resize((224, 224))
        if new_img.mode != "RGB":
            new_img = new_img.convert("RGB")
        #print(type(new_img))
        new_img.save("./preprocessed/" + "Image_" + str(i) + ".jpg")
        i= i + 1
    print("All image preprocessed and resized")


URL = "https://www.prothomalo.com/"



if __name__ == "__main__":
    #HTTP Request to Given URL
    r = requests.get(URL)
    print("Enter Number of Images you want to download...")
    number_of_images = int(input())
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    folder_create(images, number_of_images)
    resize_image()
  
  

  