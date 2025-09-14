import cv2

ash = cv2.imread("ash.png")
pikachu = cv2.imread("pikachu.png")

addimage = cv2.addWeighted(ash,0.5,pikachu,0.4, 0)

cv2.imshow("pikashu", addimage)

cv2.waitKey(0)
cv2.destroyAllWindows()