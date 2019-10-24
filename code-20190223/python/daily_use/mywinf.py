import requests
import time
import os
import ctypes

__all__ = ['gen_wall_paper']

# save imgs directory
path = 'C:\\Users\\gusto\\Desktop\\bing_pics'
img_name = time.strftime("%Y-%m-%d", time.localtime()) + '.jpg'


def get_and_save_img(url=None):
    if url is None:
        # current useable url for downloading bing.com first-page picture
        url = "https://area.sinaapp.com/bingImg/"
    pic = requests.get(url)
    if pic.status_code == 200:
        os.chdir(path)
        # There's a bug,the old picture maybe rewrite with new img
        with open(img_name, 'wb+') as f:
            f.write(pic.content)
    else:
        print("image download faield!!")


def set_img_as_wallpaper():
    pic_location = os.path.join(path, img_name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pic_location, 0)
    print("All require satisfied")


def gen_wall_paper():
    get_and_save_img()
    set_img_as_wallpaper()


gen_wall_paper()
