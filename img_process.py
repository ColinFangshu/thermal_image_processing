from src.utils import calc_temps_in_bounding_box
import cv2
import numpy as np
# from collections import Counter
import pytesseract

test_img_file = "data/thermal_images/thermal_1.png"
test_img_files = [f"data/thermal_images/thermal_{i}.png" for i in range(1, 500)]
test_bounding_box = [250, 300, 250, 300]   # in a format of bb_x_min, bb_x_max, bb_y_min, bb_y_max



if __name__ == '__main__':
    image = cv2.imread(test_img_file, 0)
    image_np = np.array(image)

    # total_read = 0
    # for file in test_img_files:
    #     print(file.split(".")[0].split("_")[-1])
    #     res = calc_temps_in_bounding_box(file, test_bounding_box)
    #     if res: total_read += 1
    #     print(res)
    # print(total_read/len(test_img_files))

    print(calc_temps_in_bounding_box(test_img_file, test_bounding_box))
    # print(pytesseract.image_to_string(image[70:100, 500:600]))
    # print("/n")
    # print(pytesseract.image_to_string(image))
    cv2.imshow('bounding box', image[test_bounding_box[0]:test_bounding_box[1], test_bounding_box[2]:test_bounding_box[3]])
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    # print("max")
    # print(pytesseract.image_to_string(image[70:100, 500:600]))
    # print("min")
    # print(pytesseract.image_to_string(image[390:420, 500:600]))
    # print("whole")
    # print(pytesseract.image_to_string(image))

    