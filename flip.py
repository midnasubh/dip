from PIL import Image
img=Image.open('C:\\DIP\\SendAnywhere_668899\\IMG-20260911-WA0007.jpg')
flip=img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('flip.jpg')

#filp top bottom
flip1=img.transpose(Image.FLIP_TOP_BOTTOM)
flip1.save('flip1.jpg')

#show the image
flip1.show()
flip.show()
