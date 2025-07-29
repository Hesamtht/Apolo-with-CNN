import sys
import cv2
import numpy as np
from keras.models import load_model
import mediapipe as mp
from PyQt5.QtCore import pyqtSignal, QObject

class GestureSignal(QObject):
    gesture_detected = pyqtSignal(int)

gesture_signal = GestureSignal()

def gesture_recognition():
    model = load_model('gesture_recognition_model.h5')

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"Error: Could not open camera.")
        sys.exit()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                flattened_landmarks = np.array([coord for point in landmarks for coord in point]).reshape(1, -1)
                prediction = model.predict(flattened_landmarks)
                predicted_mode = np.argmax(prediction)
                gesture_signal.gesture_detected.emit(predicted_mode)
                cv2.putText(frame, f'Mode: {predicted_mode}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
