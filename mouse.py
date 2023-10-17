import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
pyautogui.moveTo(screen_w // 2, screen_h // 2)
while (True):
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_f)
    landmarks_p = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmarks_p:
        landmarks = landmarks_p[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x*frame_w)
            y = int(landmark.y*frame_h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0))
            if id == 1:
                screen_x = screen_w/frame_w * x * 1.5
                screen_y = screen_h/frame_h * y * 1.5
                pyautogui.moveTo(screen_x, screen_y)

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x*frame_w)
            y = int(landmark.y*frame_h)
            cv2.circle(frame, (x, y), 2, (0, 125, 125))
        print(left[0].y - left[1].y)
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        video.release()

    cv2.imshow("EYE", frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
