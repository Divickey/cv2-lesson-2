import cv2

pikachu = cv2.imread("pikachu.png")
gaussian = cv2.GaussianBlur(pikachu, (7,7), 0)
cv2.imshow('gaussian blur', gaussian)

median = cv2.medianBlur(pikachu, 5)
cv2.imshow('median blur', median)

bilateral = cv2.bilateralFilter(pikachu, 9, 75, 75)
cv2.imshow('bilateral blur', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()