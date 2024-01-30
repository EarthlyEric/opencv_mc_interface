import cv2
import mediapipe as mp
from tkinter import messagebox

from libs.hand_pos_lib import hand_angle_hander
from libs.input_lib import hand1_pos_solver


mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
w, h = 720, 360 

camera01 = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not camera01.isOpened():
        messagebox.showinfo(title="OpenCV Minecraft Interface",message="Camera 01 can't open sucessfully")
        exit()
    
    while True:
        ret1, img1 = camera01.read()
        img1 = cv2.resize(img1, (w,h))
        if not ret1:
            messagebox.showinfo(title="OpenCV Minecraft Interface",message="Camera 01 can't open sucessfully")
            print("Cannot receive frame")
            break
        rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_img1)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []
                for i in hand_landmarks.landmark:
                    x = i.x*w
                    y = i.y*h
                    finger_points.append((x,y))
                if finger_points:
                    finger_angle = hand_angle_hander(finger_points)
                    hand1_pos_solver(finger_angle)
                mp_drawing.draw_landmarks(
                    img1,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
        cv2.imshow('camera01', img1)
        if cv2.waitKey(5) == ord('q'):
            break
camera01.release()
cv2.destroyAllWindows()