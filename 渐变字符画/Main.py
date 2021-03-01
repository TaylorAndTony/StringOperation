import cv2 as cv


def convert(resource, width0, safe_mode=False):
    # ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    ascii_char = list(r"$%Wwzr\|[]_+~^`'.    ")
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


if __name__ == '__main__':
    FILE_NAME = 'jianbian.png'
    WIDTH = 100
    result = convert(FILE_NAME, WIDTH)
    print(result)