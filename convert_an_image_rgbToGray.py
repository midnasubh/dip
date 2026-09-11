from PIL import Image
image= Image.open("pexels-optical-chemist-340351297-31284696.jpg")
gray_image= image.convert("L")
gray_image.show()
#save the gray image
gray_image.save("gray_image.jpg")