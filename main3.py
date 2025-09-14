import cv2

ash = cv2.imread("ash.png")

cv2.imshow("original image",ash)

resized = cv2.resize(ash, (300,300))

cv2.imshow("resized", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()