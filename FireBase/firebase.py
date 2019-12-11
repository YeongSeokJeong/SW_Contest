import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import numpy as np
import os
import datetime
import threading


carnumber=0
carlen=43

cred = credentials.Certificate('Mykey.json')
# firebase Autentication
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://contest-6f840.firebaseio.com'
    # 자신 DB주소로 접속.
})

ref = db.reference()
# DB의 data 받아오기


def listener(event):
    # 주차장의 .차량 변화를 보여주는 함수
    if event.data['test3']==False:
        cap = cv2.VideoCapture('./parking.mp4')
        # 동영상 실행
        if (cap.isOpened() == False): 
            print("Unable to read camera feed")
        while(True):
            ret,frame = cap.read()
            # DB정보와 동영상 frame 받아오기
            if ret == True: 
                cv2.imshow('frame',frame)
                # 현재 frame으로 실행
                if cv2.waitKey(400) & 0xFF == ord('q'):
                    # 400은 frame 속도
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows() 
    
firebase_admin.db.reference().listen(listener)
# 변화가 있을시 감지

def excute(number,carnumber):
    ref.update({'/test/realtest/car'+str(carnumber)+'/carEmpty':bool(1)})
    #firebase에 값 저장

for i in range(carlen):
            my_thread = threading.Thread(target=excute,args=(i,carnumber))
            #현재 주차장 크기만큼 값 변경
            my_thread.start()
            carnumber+=1

