import pytesseract   # https://github.com/madmaze/pytesseract
import cv2
import numpy as np

MAX_TEMP = 1000
MIN_TEMP = 0
INTENSITY_RANGE = [55, 255]   # this is the corresponding grey scale intensity range

def read_ocr_output(output):
    nums = []
    for line in output.splitlines():
        clean_line = line.strip().split(".")[0].split(" ")[0]
        if clean_line.isdigit():
            nums.append(int(clean_line))
    return sorted(nums) if min(nums) >= MIN_TEMP and max(nums) <= MAX_TEMP else []

def get_temp_range_from_thermal(path_to_file):
    image = cv2.imread(path_to_file, 0)
    outputs = pytesseract.image_to_string(image)
    temp_range = read_ocr_output(outputs)
    return temp_range

def calc_temps_in_bounding_box(img_file, bounding_box_range):
    bb_x_min, bb_x_max, bb_y_min, bb_y_max = bounding_box_range
    image = cv2.imread(img_file, 0)
    image_np = np.array(image)
    temp_scale = get_temp_range_from_thermal(img_file)
    
    print(temp_scale)
    slope = (temp_scale[1] - temp_scale[0]) / (INTENSITY_RANGE[1] - INTENSITY_RANGE[0])
    intercept = temp_scale[1] - slope*INTENSITY_RANGE[1]
    print(slope, intercept)

    pixel_intensity_in_bb = image_np[bb_x_min:bb_x_max, bb_y_min:bb_y_max].flatten()
    print(np.min(pixel_intensity_in_bb))
    min_intensity_bb = np.min(pixel_intensity_in_bb)*slope + intercept
    max_intensity_bb = np.max(pixel_intensity_in_bb)*slope + intercept
    avg_intensity_bb = np.mean(pixel_intensity_in_bb)*slope + intercept
    return (min_intensity_bb, max_intensity_bb, avg_intensity_bb)


