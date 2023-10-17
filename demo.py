import cv2
print(cv2.__version__)

#hien thi hinh anh
img = cv2.imread('digital-neon.jpg')

cv2.imshow('Display Image', img)
cv2.waitKey(0)

#lay kich thuoc anh
img = cv2.imread('digital-neon.jpg')
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))

#Output: width=580, height=326, depth=3

#lay gia tri mau o mot diem anh
(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))
#output: R=96, G=100, B=111

#cat anh
roi = img[50:350, 60:360]
cv2.imshow('Region Of Interest', roi)
cv2.waitKey(0)

#doi kich thuoc anh
img = cv2.imread('digital-neon.jpg')

(h, w, d) = img.shape

r = 300.0 / w 
dim = (300, int(h * r))

resized = cv2.resize(img, dim)

#xoay anh
img = cv2.imread('digital-neon.jpg') 
(h, w, d) = img.shape 
center = (w // 2, h // 2) 
M = cv2.getRotationMatrix2D(center, 45, 1.0) 
rotated = cv2.warpAffine(img, M, (w, h))

