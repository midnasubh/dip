from PIL import Image
image= Image.open("pexels-optical-chemist-340351297-31284696.jpg")
gray_image= image.convert("L")
threshold = 128
binary_image = gray_image.point(lambda p: 255 if p > threshold else 0)
binary_image.show()
#save the binary image
binary_image.save("binary_image.jpg")