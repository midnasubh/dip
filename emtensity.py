from PIL import Image
import numpy as np
img = Image.open('C:\\DIP\\SendAnywhere_668899\\IMG-20260911-WA0007.jpg')
img_array = np.array(img)
print(img_array.shape)