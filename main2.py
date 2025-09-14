import cv2

ash = cv2.imread("ash.png")
pikachu = cv2.imread("pikachu.png")

subtractimage = cv2.subtract(ash,pikachu)

cv2.imshow("pikashu",subtractimage)

cv2.waitKey(0)

cv2.destroyAllWindows()
