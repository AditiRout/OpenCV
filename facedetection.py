import cv2

#set library path
lib_path = 'haar/haarcascade/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(lib_path)

#open web cam (if you use usb camera change "0" to "1")
webcam = cv2.VideoCapture(0)

while True:
    
    #Start capturing Frame
    ret, frame = webcam.read()

    #Flip screen
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, minNeighbors=5, minSize=(50, 50), maxSize=(300,300))
    print(len(faces))#to get no.of faces
    

    #draw rectangle box around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #Show the capture frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()