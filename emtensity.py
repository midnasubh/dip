from PIL import Image
import numpy as np
img = Image.open('pexels-optical-chemist-340351297-31284696.jpg')
img_array = np.array(img)
print(img_array)