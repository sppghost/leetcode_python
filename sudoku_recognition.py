from PIL import Image
from pytesseract import pytesseract, image_to_string

path = 'C:\\Users\\10219\\OneDrive\\桌面\\'


def image_to_array():
    image_file = path + 'image1.png'
    im = Image.open(image_file, mode='r')
    text = image_to_string(im)
    print("=====output=======\n")
    print(text)


if __name__ == '__main__':
    image_to_array()
