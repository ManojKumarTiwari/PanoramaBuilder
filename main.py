# import necessary packages
import cv2
import os

ROOT_PATH = 'data'
dirs_in_root_path = os.listdir(ROOT_PATH)
# print(dirs_in_root_path)

for dir in dirs_in_root_path:
    file_root_path = ROOT_PATH + '/' + dir
    # print(file_root_path)
    images = []
    file_name = os.listdir(file_root_path)
    # print(file_name)
    print(f"Number of image detected: {len(file_name)}")
    for file in file_name:
        currfile = file_root_path + '/' + file
        currimg = cv2.imread(currfile)
        currimg = cv2.resize(currimg, (0,0), None, 0.2, 0.2)
        images.append(currimg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if status == cv2.Stitcher_OK:
        print("Panorama Created")
        cv2.imshow(dir, result)
        cv2.waitKey(1)
    else:
        print("Panorama Creation Unsuccessful")

cv2.waitKey(0)
