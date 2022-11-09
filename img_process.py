from src.utils import calc_temps_in_bounding_box
import cv2
import numpy as np
from collections import Counter

test_img_file = "data/thermal_images/thermal_1.png"
test_img_files = [f"data/thermal_images/thermal_{i}.png" for i in range(1, 500)]
test_bounding_box = [200, 280, 300, 340]   # in the format of bb_x_min, bb_x_max, bb_y_min, bb_y_max



if __name__ == '__main__':
    image = cv2.imread(test_img_file, 0)
    image_np = np.array(image)
    print(calc_temps_in_bounding_box(test_img_file, test_bounding_box))

