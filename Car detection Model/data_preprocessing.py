from __future__ import division
import matplotlib.pyplot as plt
import cv2
import os, glob
import numpy as np
from moviepy.editor import VideoFileClip
cwd = os.getcwd()

pixel = [[360, 369, 272, 433, 394, 442, 489, 377, '1', '1'],
         [492, 374, 394, 439, 509, 438, 605, 372, '2', '0'], 
         [575, 359, 470, 436, 607, 442, 674, 373, '3', '1'], 
         [667, 369, 594, 444, 709, 442, 768, 368, '4', '0'], 
         [758, 356, 707, 436, 819, 434, 865, 367, '5', '1'], 
         [870, 375, 806, 433, 931, 447, 960, 373, '6', '0'],
         [958, 359, 921, 444, 1030, 441, 1052, 366, '7', '1'],
         [1051, 363, 1028, 444, 1141, 442, 1136, 356, '8', '1'], 
         [1134, 352, 1139, 447, 1247, 442, 1210, 351, '9', '1'], 
         [1214, 350, 1250, 453, 1358, 450, 1304, 355, '10', '0'],
         [1319, 370, 1360, 447, 1484, 449, 1405, 352, '11', '1'], 
         [1428, 366, 1477, 452, 1579, 453, 1502, 361, '12', '0'], 
         [1522, 379, 1573, 453, 1692, 449, 1602, 358, '13', '1'], 
         [1622, 372, 1692, 451, 1791, 444, 1690, 375, '14', '0'], 
         [1708, 378, 1792, 448, 1898, 446, 1773, 368, '15', '0'], 
         
         [146, 449, 63, 516, 171, 527, 243, 451, '16', '1'], 
         [256, 447, 169, 523, 305, 525, 387, 451, '17', '1'], 
         [765, 429, 680, 536, 844, 555, 899, 444, '18', '1'], 
         [896, 445, 835, 558, 987, 560, 1010, 450, '19', '1'],
         [1018, 450, 987, 554, 1133, 558, 1132, 456, '20', '0'],
         [1133, 454, 1133, 560, 1281, 558, 1246, 453, '21', '1'],
         [1253, 456, 1283, 562, 1430, 557, 1372, 455, '22', '0'], 
         [1373, 456, 1431, 569, 1572, 564, 1481, 451, '23', '1'], 
         [1494, 455, 1578, 568, 1728, 568, 1605, 450, '24', '0'],
         [1727, 561, 1866, 562, 1778, 446, 1630, 461, '25', '1'],
        
         [153, 483, 11, 577, 154, 620, 307, 476, '26', '1'], 
         [283, 482, 146, 613, 312, 619, 440, 483, '27', '1'], 
         [429, 461, 281, 616, 474, 619, 578, 481, '28', '1'], 
         [590, 492, 466, 623, 629, 632, 703, 490, '29', '1'], 
         [704, 479, 620, 635, 793, 637, 865, 493, '30', '1'], 
         [865, 499, 791, 632, 961, 636, 997, 511, '31', '0'],
         [996, 507, 955, 634, 1142, 630, 1130, 519, '32', '1'], 
         [1135, 517, 1133, 636, 1307, 643, 1266, 508, '33', '1'],
         [1267, 502, 1305, 641, 1489, 645, 1395, 497, '34', '1'],
         [1395, 496, 1479, 644, 1638, 647, 1527, 507, '35', '0'],
         [1544, 527, 1647, 647, 1811, 646, 1664, 519, '36', '0'], 
        
         [278, 706, 78, 939, 323, 952, 520, 741, '37', '1'], 
         [550, 704, 325, 948, 572, 972, 723, 722, '38', '0'], 
         [712, 726, 572, 980, 847, 983, 929, 744, '39', '1'],
         [939, 688, 848, 989, 1124, 1002, 1130, 679, '40', '1'],
         [1132, 693, 1127, 1008, 1411, 1004, 1335, 716, '41', '1'], 
         [1329, 721, 1414, 1000, 1697, 999, 1520, 712, '42', '0'],
         [1536, 743, 1699, 1001, 1916, 999, 1764, 708, '43', '1']]

# 미리 찾은 주차공간의 좌표

pixel_list = []
label_list = []
for x1,y1,x2,y2,x3,y3,x4,y4,t,n in pixel:
    pixel_list.append([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
# 미리 찾은 주차공간의 좌표를 픽셀 리스트에 넣는다.

def show_images(images, cmap=None):
    cols = 2
    rows = (len(images)+1)//cols
    
    plt.figure(figsize=(15, 12))
    for i, image in enumerate(images):
        plt.subplot(rows, cols, i+1)
        # use gray scale color map if there is only one channel
        cmap = 'gray' if len(image.shape)==2 else cmap
        plt.imshow(image, cmap=cmap)
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout(pad=0, h_pad=0, w_pad=0)
    plt.show()

# 이미지를 보여주는 함수

def image_to_cell(images,pixel_lists = pixel_list):
    image_list = []
    for image in images:
        for re in pixel_lists:# 미리 지정한 좌표를 하나하나 불러온다.
            pix1,pix2,pix3,pix4 = re
            s_x = int(min(pix1[0],pix2[0]))
            e_x = int(max(pix3[0],pix4[0]))
            s_y = int(min(pix1[1],pix4[1]))
            e_y = int(max(pix2[1],pix3[1]))
            im = image[s_y:e_y, s_x:e_x]
            image_list.append(np.array(im))
    return image_list
# 이미지를 미리 지정한 좌표에 따라 분할하는 함수

def convert_gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# 흑백 변환

def select_rgb_white_yellow(image): 
    # white color mask
    lower = np.uint8([120, 120, 120])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(image, lower, upper)
    # 색 체크 후 범위가 아닌 경우에 색을 검은색으로 바꿈
    lower = np.uint8([190, 190,   0])
    upper = np.uint8([255, 255, 255])
    yellow_mask = cv2.inRange(image, lower, upper)
    # combine the mask
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked

# 색을 변환한다.

def make_input(images):
    model_input_image = []
    for r in images:
        step_input = []
        need_row = max_row - r.shape[0]
        need_col = max_col - r.shape[1]
        pad_row = [[0 for a in range(max_col)] for _ in range(need_row//2)]
        pad_row1 = [[0for a in range(max_col)] for _ in range(need_row - need_row//2)]
        real_value = []
        for i in r:
            step_array = i.copy()
            pad = [0 for _ in range(need_col//2)]
            pad_1 = [0 for _ in range(need_col - (need_col//2))]
            pad += step_array.tolist()
            pad += pad_1
            real_value.append(pad) 
        pad_row = pad_row +  real_value
        pad_row += pad_row1
        model_input_image.append(np.array(pad_row))
    return model_input_image
# 모델이 원하는 이미지 크기를 만들기 위해 패딩까지 하는 함수.

 