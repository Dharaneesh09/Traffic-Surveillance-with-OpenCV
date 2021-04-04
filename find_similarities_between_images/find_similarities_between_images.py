import cv2
import numpy as np

original = cv2.imread("TrafficPPT.png")
image_to_compare = cv2.imread("Target car.png")



# 1) Check if 2 images are equals
if original.shape == image_to_compare.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)
    cv2.imshow("Difference",difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are NOT equal")
		
# 2) Check for similarities between the 2 images

sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
#print(len(kp_1))
#print(desc_1)
#cv2.imshow("Desc1",cv2.resize(desc_1,(500,500)))
#cv2.imshow("Desc2",cv2.resize(desc_2,(500,500)))
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(desc_1, desc_2, k=2)

good_points = []
ratio = 0.6

for m, n in matches:
    print('',end='')
    if m.distance < ratio*n.distance :
        good_points.append(m)
print(good_points)

result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

result= cv2.resize(result,(1000,600))
cv2.imshow("result", result)
#cv2.imshow("Original", original)
#cv2.imshow("Duplicate", image_to_compare)
cv2.waitKey(0)
cv2.destroyAllWindows()