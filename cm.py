import cv2
import time

#load pre-training file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#begin the camera
camera = cv2.VideoCapture(1)
count = 0

def detectFace(frame):
    global count
    img = False
	
	#convert an image from one color space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   # detect face
    faces = face_cascade.detectMultiScale(
        gray,
		#specifying how much the image size is reduced at each image scale
        scaleFactor=1.1,
		#specifying how many neighbors each candidate rectangle should have to retain it, this parameter will affect the quality of the detected faces. Higher value results in fewer detections but with higher quality, between 3 ~ 6  is a good value
        minNeighbors=5,
		#minimum possible object size. Objects smaller than that are ignored. This parameter determines how small size you want to detect. Usually, [30, 30] is a good start for face detection.
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
	
    for (x, y, w, h) in faces:
		#create a rectangle to identify the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        img = True

    #cv2.imshow('Video', frames)
    if img:
        time.sleep(5)
		#save photo
        cv2.imwrite('C:/Users/Goncalo/final/fotos/image-'+ str(count) +'.jpg', frame)
        count+=1
    else:
        print("face dont detected!")
        


try:
    while(True):
		#read all frames 
        ret, frame = camera.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break

        detectFace(frame)

except KeyboardInterrupt:
    print("Keyboard interruption!")
	#release the capture frames
    camera.release()
    cv2.destroyAllWindows()

finally:
    print("Exit program!")
	#release the capture frames
    camera.release()
    cv2.destroyAllWindows()
