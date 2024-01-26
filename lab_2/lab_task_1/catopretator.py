import cv2
import numpy as np

def threshold_image(cat_path, cat_value):
    cat = cv2.imread(cat_path, cv2.IMREAD_GRAYSCALE)

    my_cat = np.zeros_like(cat)

    rows, cols = cat.shape
    for i in range(rows):
        for j in range(cols):
            if cat[i, j] > cat_value:
                my_cat[i, j] = 250

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("/usr/app/src/my_cat.jpg", my_cat)

cat_path = "/usr/app/src/cat.jpg"
cat_value = 128

threshold_image(image_path, value)


import os

target_folder = 'C:/artificial_intelligence/lab_2/lab_task_1/data'

os.makedirs(target_folder, exist_ok=True)

import shutil

source_path = '/usr/app/src/my_cat.jpg'

target_path = 'C:/artificial_intelligence/lab_2/lab_task_1/my_cat.jpg'

shutil.copy(source_path, target_path)

