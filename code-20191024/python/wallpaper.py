#!/usr/bin/env python3

import os
import sys
import time
#import urllib3
import requests


#t_start = time.time()


# shell script source: https://www.reddit.com/r/kde/comments/65pmhj/change_wallpaper_from_terminal/
# change the desktop wallpaper by given image path

# dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
# var Desktops = desktops();
# for (i=0;i<Desktops.length;i++) {
#         d = Desktops[i];
#         d.wallpaperPlugin = "org.kde.image";
#         d.currentConfigGroup = Array("Wallpaper",
#                                    "org.kde.image",
#                                    "General");
#        d.writeConfig("Image", "/home/$USER/Pictures/imagename.jpg");
# }'


SAVE_PATH = "/home/quan/Pictures/bing_pics"
IMAGE_NAME = time.strftime("%Y-%m-%d", time.localtime()) + ".jpg"
DEFAULT_PATH = os.path.join(SAVE_PATH, IMAGE_NAME)
IMAGE_TYPE = ('jpg', 'jpeg', 'png')
download_with_wp = "/home/quan/Pictures/download_with_wp"




def gen_cmd(abs_img_path):
    my_cmd = """dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
var Desktops = desktops();                                                                                                                       
for (i=0;i<Desktops.length;i++) {
        d = Desktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper",
                                    "org.kde.image",
                                    "General");
        d.writeConfig("Image", "IMAGE_ABS_PATH");
}'"""
    my_cmd = my_cmd.replace("IMAGE_ABS_PATH", abs_img_path)
    return my_cmd


def get_img_content(url=None):
    if url is None:
        # current useable url for downloading bing.com homepage picture
        url = "https://area.sinaapp.com/bingImg/"
    # http = urllib3.PoolManager()
    try:
        # r = http.request('GET', url)
        # return r.data
        print("here")
        r = requests.get(url)
        print(r.status_code)
        return r.content
    except:
        return b''


def save_image(abs_path, image_data):
    if os.path.exists(abs_path) or not image_data:
        return
    with open(abs_path, 'wb') as f:
        f.write(image_data)


def image_in_cwd(path):
    if any((file.endswith(IMAGE_TYPE) for file in os.listdir(path))):
        return True
    return False


def set_today():
    # there's logic bug here
    if not os.path.exists(DEFAULT_PATH):
        image_data = get_img_content()
        save_image(DEFAULT_PATH, image_data)
    set_image_as_wallpaper(DEFAULT_PATH)


def random_set_withpath(path=None):
    import random
    if path is None or not image_in_cwd(path):
        path = SAVE_PATH
    files = os.listdir(path)
    images, i = [], 0
    for file in files:
        if file.endswith(IMAGE_TYPE):
            images.append(file)
            i += 1
        if i >= 10_000:
            break
    # print(images)
    image = random.choice(images)
    img_abs_path = os.path.join(path, image)
    set_image_as_wallpaper(img_abs_path)


def set_image_as_wallpaper(img_abs_path):
    cmd = gen_cmd(img_abs_path)
    # print(cmd)
    os.system(cmd)

def is_url(url:str):
    # maybe 
    url = url.lower()
    if url.startswith('http') and url.endswith(IMAGE_TYPE):
        return True
    else:
        return False

def slide_with_path(image_dir,duration):
    if not image_in_cwd(image_dir):
        print("No image in current path,cannot operate")
        sys.exit(1)
    files = os.listdir(image_dir)
    images = list(filter(lambda x: x.endswith(IMAGE_TYPE),files))
    i,n = 0,len(images)
    image_abs_path = os.path.join(image_dir,images[i])
    set_image_as_wallpaper(image_abs_path)
    while True:
        time.sleep(duration)

        i = (i+1)%n
        image_abs_path = os.path.join(image_dir,images[i])
        set_image_as_wallpaper(image_abs_path)
if __name__ == "__main__":
    args = sys.argv
    cwd = os.getcwd()
    print(args)
    if len(args) < 2:
        random_set_withpath(cwd)
    elif len(args) ==2:
        cmd = args[1]
        abs_path = os.path.join(cwd, cmd)
        if cmd.strip().lower() == 'today':
            set_today()
        elif cmd.endswith(IMAGE_TYPE) and os.path.exists(abs_path):
            set_image_as_wallpaper(abs_path)
        elif is_url(cmd):
            image_name = cmd.split('/')[-1]
            image_abs_path = os.path.join(download_with_wp,image_name)
            if os.path.exists(image_abs_path):
                set_image_as_wallpaper(image_abs_path)
                
            else:
                print("downloading image,may take secondes")
                print(cmd)
                image_content = get_img_content(cmd)
                save_image(image_abs_path,image_content)
                set_image_as_wallpaper(image_abs_path)
        elif os.path.isdir(abs_path) and cmd not in ('no', 'bing'):
            random_set_withpath(abs_path)
        else:
            random_set_withpath()
    elif len(args) ==3:
        print(args)
        if args[2].lower().endswith(('s','seconds')):
            str_num=""
            for c in args[2].lower():
                if c in ''.join(map(str,range(10))):
                    str_num += c
            duration = int(str_num)
        else:
            duration = int(args[2])*60
        if args[1].lower() in ('c','-c','.'):
            image_dir = os.getcwd()
        else:
            
            image_dir = os.path.join(os.getcwd(),args[1])
        
        if not os.path.exists(image_dir):
            print(f"{image_dir} does not exist")
            sys.exit(1)
        slide_with_path(image_dir,duration)
    #t_end = time.time()
    #print(f"cost {t_end - t_start} s")


"""
dont use now,but keep it here:


def get_and_save_img(url=None):
    if os.path.exists(os.path.join(SAVE_PATH, IMAGE_NAME)):
        return
    if url is None:
        # current useable url for downloading bing.com homepage picture
        url = "https://area.sinaapp.com/bingImg/"
    print("Start downloading image!!")
    pic = requests.get(url)
    if pic.status_code == 200:
        os.chdir(SAVE_PATH)
        # There's a bug,the old picture maybe rewrite with new img
        with open(IMAGE_NAME, "wb") as f:
            f.write(pic.content)
        print(f"Image saved at => {os.getcwd()}/{IMAGE_NAME}")
        print("ddd")
        return os.path.join(SAVE_PATH, IMAGE_NAME)
    else:
        print("image download faield!!")
        return
"""
