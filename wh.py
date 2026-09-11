from PIL import Image
img=Image.open("C:\DIP\SendAnywhere_668899\IMG-20260911-WA0007.jpg")
w,h=img.size
total=w*h
print('width ',w,'\nheight',h,'\ntotal',total)

# netsh int ipv4 set glob defultcurhoplimit=65
# netsh int ipv6 set glob defultcurhoplimit=65