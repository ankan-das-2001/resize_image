import cv2
import os

def resizes(fname, width, height):
    image = cv2.imread(fname)
    org_height, org_width = image.shape[0:2]
    new_image = cv2.resize(image, (height, width))

    return new_image

filename = input('Enter your filename: ')
height = input('The height of the image:')
width = input('The width of the image:')
new_image = resizes("subscribe.png",int(height),int(width))
cv2.imwrite(filename,new_image)
print("Successfully executed")
