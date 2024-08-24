import cv2
import pyautogui
import mediapipe as mp

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    output = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        eye_tip = landmarks[1]
        screen_x = screen_w * eye_tip.x
        screen_y = screen_h * eye_tip.y
        pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
        if (left[0].y - left[1].y) < 0.009:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Hack Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()