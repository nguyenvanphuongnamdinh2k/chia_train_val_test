import threading
import os
import numpy
import cv2
from sklearn.model_selection import train_test_split
import shutil
def chialabel(file_label,file_save_txt,file_img):
    for txt in os.listdir(file_label):
        if ((txt.split(".txt")[0] + ".jpg") in os.listdir(file_img)):
            shutil.copy(os.path.join(file_label,txt),file_save_txt)

file_label = "mayin_update_label/labels"
file_save_txt1 = r"tong_hop_train_val/train/labels"
file_img1 = r"tong_hop_train_val/train/images"

file_save_txt2 = r"tong_hop_train_val/val/labels"
file_img2 = r"tong_hop_train_val/val/images"

threading.Thread(target=chialabel,args=(file_label,file_save_txt1,file_img1)).start()
threading.Thread(target=chialabel,args=(file_label,file_save_txt2,file_img2)).start()