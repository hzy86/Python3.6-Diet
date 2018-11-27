# Python3.6-DietSkan
DietSkan Object detection with Tensorflow. Nov 2018 - Present

Database: [ECUSTFD](https://github.com/Liang-yc/ECUSTFD-resized)

## Usage
Your folder structure should look like
```
+ Python3.6-DietSkan
	+ ECUSTFD-resized-
		+ Annotations
			-- (a lot of .xml)
		+ ImageSets
		+ JPEGImages
			-- (a lot of .JPG)
		-- other stuff in this repo
```

generate_tf_record.py

	Based on create_tf_record.py. Modified paths to generate Tensorflow records for our custom dataset.
	
unzip_tar.py
  
  Unzip a .tar or .tar.gz file in current dir.
  
generate_train_val.py

  Copy images and annotations specified in train.txt and val.txt into directory "train" and "val" in current dir, each contains a folder "JPEGImages" and a folder "Annotations".

## Reference
  [StackOverflow: Train Tensorflow Object Detection on own dataset](https://stackoverflow.com/questions/44973184/train-tensorflow-object-detection-on-own-dataset?noredirect=1&lq=1)
