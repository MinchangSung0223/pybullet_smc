import cv2
import numpy as np
import math
width = 640
height = 640


img = np.load('depth_0.922427594533084_-1.8478728346188373_99.npy')*1000
#img = cv2.imread('depth.png',cv2.IMREAD_GRAYSCALE)
print(img.max())
img[img==1000.0] = 0
print(img)
cv2.imshow('rgb',img)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)/2
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)/2
magnitude = np.sqrt(np.square(sobelx)+np.square(sobely))
#magnitude = (magnitude-magnitude.min())/(magnitude.max()-magnitude.min())
print(magnitude.min())
print(magnitude.max())
gradient_img = np.zeros((height,width));
gradient_img_rgb = np.zeros((height,width,3));
orientation = 0;
for r in range(0,height):
   for c in range(0,width):
      x = sobelx[r,c]
      y = sobely[r,c]
      w = np.sqrt(x*x+y*y)
      if w < 0.001:
         x =0
         y=0
      angle = math.atan2(y,x)*180/math.pi
      orientation =round(angle/22.5)+8
      if orientation < 0:
         print("ori : "+str(orientation)+"real :"+str(angle))
      gradient_img[r,c] = orientation*30
      if (x == 0 and y == 0):
         orientation = -1
      if orientation == -1 :
         gradient_img_rgb[r,c,:] = [0,0,0]
      elif orientation == 0 :
         gradient_img_rgb[r,c,:] =[0,0,255]
      elif orientation == 1 :
         gradient_img_rgb[r,c,:] = [127,0,255]
      elif orientation == 2 :
         gradient_img_rgb[r,c,:] = [255,0,255]
      elif orientation == 3 :
         gradient_img_rgb[r,c,:] = [255,0,127]
      elif orientation == 4 :
         gradient_img_rgb[r,c,:] = [255,0,64]
      elif orientation == 5 :
         gradient_img_rgb[r,c,:] = [255,0,0]
      elif orientation == 6 :
         gradient_img_rgb[r,c,:] = [255,64,0]
      elif orientation == 7 :
         gradient_img_rgb[r,c,:] = [255,127,0]
      elif orientation == 8 :
         gradient_img_rgb[r,c,:] = [255,255,0]
      elif orientation == 9 :
         gradient_img_rgb[r,c,:] = [127,255,0]
      elif orientation == 10 :
         gradient_img_rgb[r,c,:] = [64,255,0]
      elif orientation == 11 :
         gradient_img_rgb[r,c,:] = [0,255,127]
      elif orientation == 12 :
         gradient_img_rgb[r,c,:] = [0,255,64]
      elif orientation == 13 :
         gradient_img_rgb[r,c,:] = [0,255,255]
      elif orientation == 14 :
         gradient_img_rgb[r,c,:] = [0,127,255]
      elif orientation == 15 :
         gradient_img_rgb[r,c,:] = [0,0,255]


#print(gradient_img[462:472,343:353])
#print("---------------")
#print(magnitude)
cv2.imshow('sobelx',sobelx*255)
cv2.imshow('sobely',sobely*255)
cv2.imshow('magnitude',magnitude*4)
#cv2.imshow('gradient_img',np.uint8(gradient_img))
cv2.imshow('gradient_img_rgb',np.uint8(gradient_img_rgb))

'''
print(gradient_img.shape)
ret, img_binary = cv2.threshold(np.uint8(img.copy()), 127, 255, 0)
print(img_binary.shape)
contours, hierachy = cv2.findContours(img_binary[:,:,1].copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
max_area = 0
area_threshold = 5000
max_cnt = 0
for cnt in contours:
  M = cv2.moments(cnt)
  if max_area < M['m00']: 
    max_area = M['m00']
    max_cnt = cnt
c0 = max_cnt
print(max_area)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print("cx :",cx)
print("cy :",cy)
for cnt in contours:
    hull = cv2.convexHull(cnt)
contour_img = cv2.drawContours(img.copy(), contours, -1, (255,0,0), 2)
cv2.circle(contour_img, (cx, cy), 5, (0,0,255), 0)
cv2.imshow('contour_img',contour_img)
'''
cv2.waitKey(0)
