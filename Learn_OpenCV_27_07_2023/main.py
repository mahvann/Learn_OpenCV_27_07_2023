import cv2

img = cv2.imread(r"media\\rose.png")
anh_xam = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Anh xam",anh_xam)

cv2.waitKey()