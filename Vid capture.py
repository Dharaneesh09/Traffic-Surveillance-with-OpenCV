import cv2,time

video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    print(check,end='')
    #frame= cv2.resize(frame,(500,500))
    cv2.imshow('Capture',frame)
    #print(frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
'''
img = cv2.imread('C:\\Users\\DHARANEESH\\Pictures\\Saved Pictures\\The Lion.jpg')
img=cv2.resize(img,(500,700))
cv2.imshow("Lion",img)
cv2.waitKey(0)
'''
