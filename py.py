import cv2
import numpy as np
original = cv2.imread(r"C:\Users\Kishore\Computer vision__ OPenCV\images\1 ST high ac CERVICITIS T3 S3.jpg")
duplicate = cv2.imread(r"C:\Users\Kishore\Computer vision__ OPenCV\images\1 ST high ac CERVICITIS T3 S3.jpg")
# 1) Check if 2 images are equals
if original.shape == duplicate.shape:
   print("The images have same size and channels")
   difference = cv2.subtract(original, duplicate)
   b, g, r = cv2.split(difference)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("The images are completely Equal")
cv2.imshow("Original", original)
cv2.imshow("Duplicate", duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()