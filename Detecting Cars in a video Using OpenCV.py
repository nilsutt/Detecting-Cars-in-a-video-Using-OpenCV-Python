import cv2
cars="cars.xml"
video="video1.avi"
kamera=cv2.VideoCapture(video)
cars_detector=cv2.CascadeClassifier(cars)

while True:
    ret, frame=kamera.read()
    if type(frame)==type(None):
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    car=cars_detector.detectMultiScale(gray,1.1,1)
    for (i,(x,y,w,h)) in enumerate(car):
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,"Car {}".format(i+1),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.55,(255,0,0),2)
    cv2.waitKey(33)

kamera.release()
cv2.destroyAllWindows()