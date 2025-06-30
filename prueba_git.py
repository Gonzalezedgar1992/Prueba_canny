import cv2
img= cv2.imread('panel-solar.jpg')
bordeCanny=cv2.Canny(img, 50,100)
cv2.imshow('Original', img)
cv2.imshow('Canny - min=100, max=200', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
