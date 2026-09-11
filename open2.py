import cv2

# 1. Added quotes around the file path
img = cv2.imread("C:\\DIP\\SendAnywhere_668899\\IMG-20260911-WA0007.jpg")

# 2. Added quotes around the window name
cv2.imshow("output", img)

# 3. Capitalized the 'K' in waitKey and adjusted the time
cv2.waitKey(0)
