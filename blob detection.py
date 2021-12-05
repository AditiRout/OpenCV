import cv2

vid=cv2.VideoCapture(0)

while True:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)
    im=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    para=cv2.SimpleBlobDetector_Params()
    para.filterByArea=True
    para.minArea=100
    para.maxArea=200
    detector=cv2.SimpleBlobDetector(para)
    #Key=detector.detect(im)
    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(im, None)
    # compute the descriptors with ORB
    kp, des = orb.compute(im, kp)
    im_points=cv2.drawKeypoints(frame,kp,0,(0,0,255))
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    cv2.imshow("Keypoints", im_points)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows
