import cv2

pikachu = cv2.imread("pikachu.png")

borderedimage = cv2.copyMakeBorder(pikachu, 50, 50 ,0, 0, cv2.BORDER_CONSTANT, value = 1)

cv2.imshow("border",borderedimage)



cv2.waitKey(0)
cv2.destroyAllWindows()