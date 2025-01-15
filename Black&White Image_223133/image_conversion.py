from PIL import Image
import numpy as np


image_path = 'images/enhanced.png'
image = Image.open(image_path)


threshold = 128  # set a threshold to define white vs black
image_bw = image.convert('L').point(lambda x: 255 if x > threshold else 0, mode='1')

# Calculate the number of pixels before and after conversion
original_pixels = np.array(image).size
bw_pixels = np.array(image_bw).size

# Save the black and white image
bw_image_path = 'images/image_bw.png'
image_bw.save(bw_image_path)

print("Number of pixels in the original image:", original_pixels)
print("Number of pixels in the black and white image:", bw_pixels)
print("Black and white image saved at:", bw_image_path)