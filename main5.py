import cv2
import numpy as np

pikachu = cv2.imread("pikachu.png")
krnl = np.ones((3,3), np.uint8)
erosion = cv2.erode(pikachu, krnl)

cv2.imshow("ERODED" ,erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()