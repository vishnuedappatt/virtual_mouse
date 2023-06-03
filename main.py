import cv2
import mediapipe as mp
import pyautogui


capture=cv2.VideoCapture(0)

hd=mp.solutions.hands.Hands()
draw=mp.solutions.drawing_utils
s_w ,s_h =pyautogui.size()
index_y=0
while True:
    _,frame= capture.read()
    frame=cv2.flip(frame,1)
    f_h,f_w,_ =frame.shape
    rgb_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    op=hd.process(rgb_frame)
    hands=op.multi_hand_landmarks
    if hands:
        for x in hands:
            draw.draw_landmarks(frame,x)
            land_m=x.landmark
            for j,k in enumerate(land_m):
                x=int(k.x*f_w)
                y=int(k.y*f_h)
                # print(x,y)
                if j == 4 :
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=s_w/f_w*x
                    index_y=s_h/f_h*y
                    pyautogui.moveTo(index_x,index_y)
                if j == 8 :
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=s_w/f_w*x
                    thumb_y=s_h/f_h*y
                    if abs(index_y-thumb_y) <20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    # print(hands)
    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)
