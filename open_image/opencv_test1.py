import cv2

img = cv2.imread("IOU.png",1)
print("img.shape =", img.shape)
cv2.imshow("Sample Image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
