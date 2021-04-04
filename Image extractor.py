import cv2
vedio= cv2.VideoCapture("Pexels Videos 2675512.mp4")
while True:
    _,frame=vedio.read()
    fr=cv2.resize(frame,(700,600))
    cv2.imshow("Frame",fr)
    key=cv2.waitKey(0)
    if key==ord('s'):
        cv2.imwrite("Image1.png",frame)
    elif key==ord('p'):
        key=cv2.waitKey(0)
        if key == ord('s'):
            cv2.imwrite("Image1.png", frame)
    elif key==ord('q'):
        break
vedio.release()
cv2.destroyAllWindows()