import os
import numpy
import cv2
from sklearn.model_selection import train_test_split
import shutil
# khai bao 2 list X,y(images,labels)

X = []
y =[]

# lặp qua các  thư mục để append ảnh vào labels vào X, y

#giả sử các folder nằm trong thư mục data

data_folder = 'mayin_update_label/images'

# tạo size ảnh muốn
# img_size = 128

# for folder in os.listdir(data_folder): # duyệt từng folder trong folder data
#     curr_path = os.path.join(data_folder,folder)  # dùng để nối 2 đường dẫn với nhau
for file in os.listdir(data_folder):   # duyệt từng ảnh trong các foler nhỏ của folder data
      # dùng để nối 2 đường dẫn với nhauv
    # images = cv2.imread(curr_file)      # đọc từng ảnh trong folder nhỏ
    # images = cv2.resize(images,(img_size,img_size))   # resize
    X.append(file)    #thêm ảnh vào list X
    y.append("img")         #thêm labels vào list y
print("total len: ",len(X))

# chia tập train test
#
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,shuffle=True)
for file in X_train:
    shutil.copy(os.path.join(data_folder,file),"tong_hop_train_val/train/images")
for file in X_test:
    shutil.copy(os.path.join(data_folder,file),"tong_hop_train_val/val/images")
print("train len",len(X_train))
# print("test len", len(y_test))


