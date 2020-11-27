import cv2

file_name = "cho.jpg"

#load image from current dir
image = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)

#descale image 50% of the original width and height
img_width = int(image.shape[1]/2)
img_heighr = int(image.shape[0]/2)

#new dimension image size
d_size = (img_width, img_heighr)

#resize our image with new dim size
output = cv2.resize(image, d_size)

#writing the output to a local image file
cv2.imwrite('img_out.jpg', output)