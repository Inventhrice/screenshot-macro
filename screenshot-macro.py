import argparse
import os
import tempfile

import pyautogui
import img2pdf


def screenshot(top_left, right_bottom, next_page, total_page):
    rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
    images = []
    temp_dir = tempfile.mkdtemp()

    for i in range(total_page):
        page_num = "{}".format(i).zfill(len(str(total_page)))
        file_name = os.path.join(temp_dir, 'book-page-{}.png'.format(page_num))
        images.append(file_name)


        #autopy.mouse.move(*next_page)
        #autopy.mouse.click(delay=1)
        pyautogui.screenshot(file_name, region=(top_left[0], top_left[1], rect_size[0], rect_size[1]))
        pyautogui.click(x=next_page[0],y=next_page[1],interval=1)
        #autopy.bitmap.capture_screen((top_left, rect_size)).save(file_name)

    return images


def image2pdf(images, filename = "book.pdf"):
    with open(filename, "wb") as f:
        f.write(img2pdf.convert(images))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take book screenshots.')
    parser.add_argument('top_left', type=str)
    parser.add_argument('right_bottom', type=str)
    parser.add_argument('next_button', type=str)
    parser.add_argument('total_page', type=int)
    parser.add_argument('file_name', type=str)

    args = parser.parse_args()

    top_left = tuple(map(lambda x: int(x), args.top_left.split(',')))
    right_bottom = tuple(map(lambda x: int(x), args.right_bottom.split(',')))
    next_button = tuple(map(lambda x: int(x), args.next_button.split(',')))
    total_page = args.total_page
    file_name = args.file_name

    print("Taking screenshot for {} from {} {} with next button at {} for {} pages".format(
        file_name, top_left, right_bottom, next_button, total_page
    ))

    images = screenshot(top_left, right_bottom, next_button, total_page)
    image2pdf(images)

    print("Done, book saved in " + file_name + ".")
