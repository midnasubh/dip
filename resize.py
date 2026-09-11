from PIL import Image
image= Image.open("C:\\DIP\\SendAnywhere_668899\IMG-20260911-WA0007.jpg")
image.show()
print("image size:",image.size)
resized=image.resize((50,100))
resized.save("resize.jpg")
resized.show()