import os
import shutil

DATA_DIR = 'ECUSTFD-resized-'
set_path = os.path.join(DATA_DIR, 'ImageSets', 'Main')
annotation_src = os.path.join(DATA_DIR, 'Annotations')
img_src = os.path.join(DATA_DIR, 'JPEGImages')

def separate(type):
    # create a new mother dir in the current dir
    if not (os.path.exists(type) and os.path.isdir(type)):
        os.mkdir(type)
    # create an Annotations and a JPEGImages dirs in the mother dir
    annotation_dest = os.path.join(type, 'Annotations')
    img_dest = os.path.join(type, 'JPEGImages')
    if not (os.path.exists(annotation_dest) and os.path.isdir(annotation_dest)):
        os.mkdir(annotation_dest)
    if not (os.path.exists(img_dest) and os.path.isdir(img_dest)):
        os.mkdir(img_dest)
    # read the .txt for the type of operation
    path = os.path.join(DATA_DIR, 'ImageSets', 'Main', type + '.txt')
    with open(path) as entries:
        for img_name in entries:
            img_name = img_name.strip('\n')
            # get the .xml for the image from annotation_src folder
            target_img = os.path.join(annotation_src, img_name + '.XML')
            shutil.copy2(target_img, annotation_dest)
            target_img = os.path.join(img_src, img_name + '.JPG')
            shutil.copy2(target_img, img_dest)

if __name__ == '__main__':
    separate('train')
    separate('val')
