
import cv2
import serial
import time
from cvzone.HandTrackingModule import HandDetector

# CHANGE COM PORT IF NEEDED
arduino = serial.Serial('COM7', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.6, maxHands=1)

while True: 
    success, img = cap.read()
    if not success:
        print("Camera error")
        break
 
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0] 
        fingers = detector.fingersUp(hand)   # [Thumb, Index, Middle, Ring, Little]

        data = ",".join(str(f) for f in fingers)
        arduino.write((data + "\n").encode())

        print("Sent:", data)

    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()