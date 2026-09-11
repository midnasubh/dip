import cv2

# 1. Added 'r' for a raw string so Windows backslashes are handled correctly
image = cv2.imread(r"C:\DIP\SendAnywhere_668899\IMG-20260911-WA0007.jpg")

# Check if the image loaded successfully before processing
if image is not None:
    # 2. Crops the image: rows 100 to 400, columns 150 to 450
    cropped = image[100:400, 150:450]

    # 3. Added window name strings as the first argument
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped)

    # 4. Added a filename string as the first argument
    cv2.imwrite("cropped_output.jpg", cropped)

    cv2.waitKey(0)
