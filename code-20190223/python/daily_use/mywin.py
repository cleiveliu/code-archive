import requests
import time
import os
import ctypes

"""
if you want ugly and unclean and shitty code:
    look_at_this()
"""


class mywin:
    def __init__(self):
        self.path = "C:\\Users\\gusto\\Desktop\\bing_pics"
        self.img_name = time.strftime("%Y-%m-%d", time.localtime()) + ".jpg"

    def gen_wall_paper(self):
        self.get_and_save_img()
        self.set_img_as_wallpaper()

    def get_and_save_img(self, url=None):
        if url is None:
            # current useable url for downloading bing.com first-page picture
            url = "https://area.sinaapp.com/bingImg/"
        pic = requests.get(url)
        if pic.status_code == 200:
            os.chdir(self.path)
            # There's a bug,the old picture maybe rewrite with new img
            with open(self.img_name, "wb+") as f:
                f.write(pic.content)
        else:
            print("image download faield!!")

    def set_img_as_wallpaper(self):
        pic_location = os.path.join(self.path, self.img_name)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, pic_location, 0)
        print("All require satisfied")
