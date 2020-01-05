import cv2

img = cv2.imread('depth.png')
sobel_img = cv2.Sobel(img,-1,1,1)
print(sobel_img.shape)
print(sobel_img.max())
cv2.imshow('rgb',sobel_img)
cv2.waitKey(2)
