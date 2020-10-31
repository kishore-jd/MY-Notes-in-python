import cv2
img =cv2.imread (r"C:\Users\Kishore\Computer vision__ OPenCV\images\1 ST high ac CERVICITIS T3 S3.jpg",0)
resized_image = cv2.resize(img, (650,500))

cv2.imshow("myimage",resized_image)
cv2.waitkey(0)

cv2.destroyAllWindows()