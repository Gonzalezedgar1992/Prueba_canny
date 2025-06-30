#Nombre paquete
import cv2
#abrir imagen 
img= cv2.imread('panel-solar.jpg')
# utilizar Canny
bordeCanny=cv2.Canny(img, 50,100)
#Graficar imagen original y bordes
cv2.imshow('Original', img)
cv2.imshow('Canny - min=100, max=200', bordeCanny)
#presionar tecla para dejar de ejecutar
cv2.waitKey(0)
cv2.destroyAllWindows()
