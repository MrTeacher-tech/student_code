import cv2
import time

THRESHOLD = 110000

RECORDTIME = 1.5

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Python Programs/output.avi', fourcc, 20.00, (640, 480))
previousIm = cv2.resize(cam.read()[1],(int(int(cam.read()[1].shape[1])*0.25),int(int(cam.read()[1].shape[0])*0.25)))

while True:
    result,im = cam.read()
    im = cv2.resize(im,(int(int(im.shape[1])*0.25),int(int(im.shape[0])*0.25)))
    imChange = cv2.subtract(im,previousIm)
    
    previousIm=im
    if cv2.waitKey(1) == ord("q"):
        break
    sumImage = 0
    
    for i in imChange:
        for x in i:
            for t in x:
                sumImage += t
    
    if sumImage > THRESHOLD:
        

        cv2.imshow("Image",cam.read()[1])

        t_end = time.time() + RECORDTIME
        while time.time() < t_end:
            out.write(cam.read()[1])
            cv2.imshow("Image",cam.read()[1])


    else:
        cv2.imshow("Image",cv2.resize(imChange,(int(int(imChange.shape[1])*4),int(int(imChange.shape[0])*4))))
    

out.release()
cam.release()
cv2.destroyAllWindows()