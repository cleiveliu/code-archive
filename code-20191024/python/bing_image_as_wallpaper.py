#!/usr/bin/env python
import os
import requests
import time

t_start = time.time()

# import ctypes

# save imgs directory
# path = 'C:\\Users\\gusto\\Desktop\\bing_pics'
path = "/home/quan/Pictures/bing_pics"
img_name = time.strftime("%Y-%m-%d", time.localtime()) + ".jpg"


def get_and_save_img(url=None):
    if url is None:
        # current useable url for downloading bing.com homepage picture
        url = "https://area.sinaapp.com/bingImg/"
    print("Start downloading image!!")
    pic = requests.get(url)
    if pic.status_code == 200:
        os.chdir(path)
        # There's a bug,the old picture maybe rewrite with new img
        with open(img_name, "wb") as f:
            f.write(pic.content)
        print(f"Image saved at => {os.getcwd()}/{img_name}")
    else:
        print("image download faield!!")


"""
def set_img_as_wallpaper():
    pic_location = os.path.join(path, img_name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pic_location, 0)
    print("OK!All require satisfied")

"""
if __name__ == "__main__":
    get_and_save_img()
    t_end = time.time()
    print(f"it cost {t_end - t_start} s")
    # set_img_as_wallpaper()
