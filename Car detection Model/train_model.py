import data_preprocessing as dp
import make_model
import numpy as np
from sklearn.model_selection import train_test_split
import os
from keras.utils import to_categorical
import cv2

def main():
	pixel_list = dp.pixel_list
	file_list = os.listdir("./image")

	for i in range(len(file_list)):
	    file_list[i] = './image/'+ file_list[i]

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
	image_file = []

	for file_name in file_list:
	    img = cv2.imread(file_name)
	    image_file.append(img)
    white_yellow_images = list(map(dp.select_rgb_white_yellow, image_file))
	gray_images = list(map(dp.convert_gray_scale, white_yellow_images))
	gray_images = dp.image_to_cell(gray_images)
	model_input_image = np.array(dp.make_input(gray_images,max_row,max_col))
	model_input_image = model_input_image.reshape((-1,max_row,max_col,1))
	lab1 = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
	lab2 = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
	label_list = np.array(lab1 * 26 + lab2 *(43-26))
	label_list = to_categorical(label_list)
	x_train,x_test,y_train,y_test = train_test_split(model_input_image,label_list,test_size = 0.3)
	model = make_model.define_model(max_row,max_col)
	model.fit([x_train],y_train,epochs = 'number',batch_size = 'batch_size')
	model.save_weights("model.h5")

if __name__ = '__main__':
	main()