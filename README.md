# Python3.6-DietSkan
DietSkan Object detection with Tensorflow. 11-25-2018

Database worked with: ECUSTFD https://github.com/Liang-yc/ECUSTFD-resized

generate_tf_record.py
  
  Based on create_tf_record.py. Modified paths to generate Tensorflow records for our custom dataset.
  
unzip_tar.py
  
  Unzip a .tar or .tar.gz file in current dir.
  
generate_train_val.py

  Copy images and annotations specified in train.txt and val.txt into directory "train" and "val" in current dir, each contains a folder "JPEGImages" and a folder "Annotations".
