from PIL import Image
image= Image.open("C:\\DIP\\SendAnywhere_668899\IMG-20260911-WA0007.jpg")
rot=image.rotate(654645)
rot.save("rotate.jpg")
rot.show()