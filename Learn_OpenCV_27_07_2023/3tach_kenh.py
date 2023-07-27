import cv2

anh = cv2.imread("media\\ronaldo.png")

img = cv2.resize(anh,(300,500))
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]
#
# cv2.imshow("img",img)
# cv2.imshow("blue",b)
# cv2.imshow("Green",g)
# cv2.imshow("Red",r)


a = img[0:int(img.shape[0]/2),0:int(img.shape[1]/2)]
print(img.shape)
print(img.size)
print(img.dtype)
cv2.imshow("a",a)
cv2.waitKey()
