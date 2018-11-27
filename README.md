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

The following list explains the .py scripts. Some functions have terminal commands that you can copy and paste, but be sure to modify the values for the arguments if needed. Explanations for the arguments are provided at the top of the command in the format like
``` 
attribute={$Explanation}
```
- **generate_tf_record.py**

	Based on create_tf_record.py. Modified paths to generate Tensorflow records for our custom dataset.
	``` terminal
	label_map_path={$Absolute or relative path to the label_map_path.pbtxt}
	data_dir={$Absolute or relative path to the data folder}
	set={$A value from [train, val, trainval, test] where 'val' stands for validation}
	output_path={$Absolute or relative path of where you want to place the output}
	
	python generate_tf_record.py \
	--label_map_path=./pascal_label_map.pbtxt \
	--data_dir=./ECUSTFD-resized- \
	--set==train  \
	--output_path=./train.record
	```

- **unzip_tar.py**
  
	 Unzip a .tar or .tar.gz file in current dir.
  
- **generate_train_val.py**

	 Copy images and annotations specified in train.txt and val.txt into directory "train" and "val" in current dir, each contains a folder "JPEGImages" and a folder "Annotations".

## Reference
  [StackOverflow: Train Tensorflow Object Detection on own dataset](https://stackoverflow.com/questions/44973184/train-tensorflow-object-detection-on-own-dataset?noredirect=1&lq=1)
