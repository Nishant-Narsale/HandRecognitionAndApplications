# imports
import keyboard
import webbrowser
import time
import cv2
import HandTrackingModule as htm
import math


# button pressing
def press_space():
    print('space pressed')
    keyboard.press('space')
    keyboard.release('space')

def press_enter():
    keyboard.press('enter')
    keyboard.release('enter')

def press_down():
    keyboard.press('down arrow')
    keyboard.release('down arrow')


# url in chrome
url = 'https://chromedino.com/'

webbrowser.get().open_new(url)
time.sleep(2)


# hand detection operations
cap_width = 200
cap_height = 200
camera = 0

cap = cv2.VideoCapture(camera)

cap.set(3, cap_width)
cap.set(4, cap_height)

detector = htm.HandDetector()

hand_open = False
jumping = False

while True:
    success, img = cap.read()

    detector.drawHands(img)

    lmList = detector.findPosition(img, draw=False)

    if lmList:
        tip_of_fingers = [lmList[i] for i in range(8,21,4)]
        wrist = lmList[0]

        sum_of_distances = 0
        for tip in tip_of_fingers:
            sum_of_distances += math.dist(wrist[1:] , tip[1:])

        avg = sum_of_distances/4
        print(avg)

        if avg<100:
            hand_open = False
            jumping = False
        else:
            hand_open = True

    if hand_open and not jumping:
        press_space()
        jumping = True


    cv2.imshow(f"Camera {camera}:",img)
    cv2.waitKey(1)




