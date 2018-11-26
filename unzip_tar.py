import tarfile

filename = "faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28.tar.gz"
if (filename.endswith("tar.gz")):
    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall()
        tar.close()
elif (filename.endswith("tar")):
    with tarfile.open(filename, "r:") as tar:
        tar.extractall()
        tar.close()
