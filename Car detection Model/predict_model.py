from data_preprocessing import *
from make_model import *
max_row = 0
max_col = 0
min_row = 0
min_col = 0
for re in pixel_list:
    pix1,pix2,pix3,pix4 = re
    s_x = int(min(pix1[0],pix2[0]))
    e_x = int(max(pix3[0],pix4[0]))
    s_y = int(min(pix1[1],pix4[1]))
    e_y = int(max(pix2[1],pix3[1]))
    step_col = e_x - s_x
    step_row = e_y - s_y
    max_row = step_row if step_row > max_row else max_row
    max_col = step_col if step_col > max_col else max_col
model = define_model(max_row,max_col)
model.load_weights("model.h5")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import numpy as np
import os
import datetime

cred = credentials.Certificate('Mykey.json')

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://contest-6f840.firebaseio.com'
})
ref = db.reference()
ref.update({'/test3':bool(1)})
import threading
def excute(number,carnumber):
    ref.update({'/test/realtest/car'+str(carnumber)+'/carEmpty':bool(number)})
    import cv2
import numpy as np
import os
import datetime
import time
# Create a VideoCapture object
cap = cv2.VideoCapture('./parking.mp4')
while_count = 0
# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Unable to read camera feed")
 # We convert the resolutions from float to integer.
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
cnt=0
while(True):
    ret,frame = cap.read()
    cnt+=1
    if cnt%3 != 0:
        continue
    
    if ret == True: 
#         now = datetime.datetime.now().strftime("%d_%H-%M-%S") 

        ret = cap.set(3,1080)
        ret = cap.set(4,1920)
    # Display the resulting frame    
       # cv2.imshow('frame',frame)
        #path='C:/Users/naya2/Desktop/data/image'
    # Press Q on keyboard to stop recording
        if ref.child('test3').get()==True:
            ref.update({'/test3':bool(0)})
        if cv2.waitKey(99) & 0xFF == ord('q'):
             break
        if cv2.waitKey(99) & 0xFF:
            print("step",while_count)
            white_yellow_images = select_rgb_white_yellow(frame)
            gray_images = convert_gray_scale(white_yellow_images)
            print(gray_images.shape)
            
            pix1,pix2,pix3,pix4 = pixel_list[0]
            s_x = int(min(pix1[0],pix2[0]))
            e_x = int(max(pix3[0],pix4[0]))
            s_y = int(min(pix1[1],pix4[1]))
            e_y = int(max(pix2[1],pix3[1]))
            print(gray_images[s_y:e_y, s_x:e_x])
            
            gray_images = image_to_cell_one(gray_images,pixel_list)
            model_input_image = make_input(gray_images,max_row,max_col)
            model_input_image = np.array(model_input_image).reshape((43,max_row,max_col,1))
            output = list(np.argmax(model.predict(model_input_image),axis = 1))
            carnumber=0
            while_count += 1
            for i in output:   
                my_thread = threading.Thread(target=excute,args=(i,carnumber))
                my_thread.start()
                carnumber+=1
            # Break the loop
        # time.sleep(1)
    else:
         break 
 
 # When everything done, release the video capture and video write objects
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows() 

