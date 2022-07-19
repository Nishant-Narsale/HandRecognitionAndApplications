import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime=0
cTime=0


while True:
    success, img = cap.read()

    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                height,width,channels = img.shape
                x, y = int(lm.x*width), int(lm.y*height)
                # if id==4:
                #     cv2.circle(img, (x,y), 5, (255,0,255), 2)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,60), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

    cv2.imshow("Image :",img)
    cv2.waitKey(1)

    if cv2.waitKey(32) == 32:
        break
    
