import cv2

path1 = "media\\ronaldo.png"
path2 = "media\\opencv.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

img1_resize = cv2.resize(img1,(300,300))
img2_resize = cv2.resize(img2,(300,300))

dest_and = cv2.bitwise_not(img1_resize,img2_resize,mask=None)

cv2.imshow("Ronaldo",img1_resize)
cv2.imshow("OpenCV",img2_resize)
cv2.imshow("Anh bitwise_and",dest_and)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
