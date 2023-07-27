import cv2

path = "media\\rgb.png"
image = cv2.imread(path)

B,G,R = cv2.split(image)
cv2.imshow("Anh Goc",image)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.waitKey()
