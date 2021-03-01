import time
import cv2 as cv
import os


def convert(resource, width0, safe_mode=False):
    # ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    ascii_char = list(r"$%W*hdwOLUzunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.    ")
    safe_char = list(r"$@B%8&WM#*o`'. ")
    lenth = len(ascii_char)

    img = cv.imread(resource, 0)
    height = img.shape[0]  # 1080
    width = img.shape[1]  # 1920
    tar_width_ratio = int(width / width0)
    resized = cv.resize(
        img, (int(width / tar_width_ratio), int(height / tar_width_ratio / 3))
    )

    text = ''
    for each_row in resized:
        for each_pix in each_row:
            if safe_mode:
                text += safe_char[int(each_pix / 256 * lenth)]
            else:
                text += ascii_char[int(each_pix / 256 * lenth)]
        text += '\n'
    return text


def read_all_4_frame():
    f1 = convert('remm 0.png', 60)
    f2 = convert('remm 1.png', 60)
    f3 = convert('remm 2.png', 60)
    f4 = convert('remm 3.png', 60)
    return f1, f2, f3, f4


if __name__ == '__main__':
    fr1, fr2, fr3, fr4 = read_all_4_frame()
    os.system('cls')
    while True:
        for i in [fr1, fr2, fr3, fr4]:
            os.system('cls')
            print(i)
            time.sleep(.1)