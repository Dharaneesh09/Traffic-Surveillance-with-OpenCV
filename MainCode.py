import cv2

# taking vedios & images for input
video = cv2.VideoCapture("Pexels Videos 2675512.mp4")
first_frame = cv2.imread("Image.png", 0)
target = cv2.imread("Target car1.png")
print("'q' for Quit, 'p' for Pause and 'f' for first frame change")

def find_obj(tar, obj):
    orb = cv2.ORB_create(nfeatures=1000)
    kp1, des1 = orb.detectAndCompute(obj, None)
    kp2, des2 = orb.detectAndCompute(tar, None)

    flann = cv2.BFMatcher()
    matches = flann.knnMatch(des1, des2, k=2)

    good = []

    ratio = 0.7
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append(m)
            if len(good) > 15:
                print(len(good))
                # cv2.waitKey(0)

    sim_img = cv2.drawMatches(obj, kp1, tar, kp2, good, None)

    cv2.imshow("com img", sim_img)
    #    cv2.waitKey(0)
    return len(good)


while True:
    # reading frames in video
    check, frame = video.read()
    if not check:
        break

    # converting them to gray scale and blurring them
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # for edged image
    #    edged = cv2.Canny(gray, 30, 255)
    #    edged = cv2.resize(edged, (600, 600))
    #    cv2.imshow("Edged", edged)

    # if no image present takes first frame as reference
    if first_frame is None:
        first_frame = gray
        continue

    # constructing an abolute difference frame
    deltaFrame = cv2.absdiff(first_frame, gray)
    #    cv2.imshow("abs diff",cv2.resize(deltaFrame,None,fx=0.4,fy=0.4))

    # dividing into two seperate elements as backgraound and object
    thresh_delta = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)  # iterations can merge nearer countours
    # if you are not using gray frames
    # thresh_delta=cv2.cvtColor(thresh_delta,cv2.COLOR_BGR2GRAY)
    # print(thresh_delta)

    # getting the object dimensions seperately
    (cnts, a) = cv2.findContours(thresh_delta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # for viewing the threshold difference frame
    #    thresh_delta = cv2.resize(thresh_delta,None,fx=0.4,fy=0.4)
    #    cv2.imshow("delta", thresh_delta)

    # i=1

    # irterating over contours
    for contour in cnts:
        # checking if the area is large enough so we don't consider noises and other tiny stuff
        area = cv2.contourArea(contour)
        #        print(area)
        if area < 5000 or area > 20000:
            continue

        # for getting the dimensions of rectangle around the objects and drawing it
        (x, y, w, h) = cv2.boundingRect(contour)
        x = (x - 20) if (x - 20 > 0) else x
        y = (y - 20) if (y - 20 > 0) else y
        x1 = x + w
        y1 = y + h
        x1 = (x1 + 20) if (x1 + 20 < len(frame[0])) else x1
        y1 = (y1 + 20) if (y1 + 20 < len(frame)) else y1
        if (find_obj(target, frame[y:y1, x:x1]) > 15):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)

        # obj=frame[y:y+h,x:x+h]
        # cv2.resize(obj,(500,500))
        # cv2.imshow("obj"+str(i),obj)
        # i+=1

    # resizing the main frame to 60%
    frame = cv2.resize(frame, None, fx=0.6, fy=0.60)
    cv2.imshow("motion", frame)

    # resizing the first frame
    #fst=cv2.resize(first_frame,(500,500))
    #cv2.imshow("First",fst)

    # viewing the frame for 1 milli second and checking for input
    key = cv2.waitKey(1)

    # breaking if q is pressed
    if key == ord('q'):
        break
    # pausing if p is pressed
    elif key == ord('p'):
        cv2.waitKey(0)
    # changing first frame if f is pressed
    elif key == ord('f'):
        first_frame = gray

video.release()
cv2.destroyAllWindows()