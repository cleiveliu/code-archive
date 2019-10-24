import os
import shutil
preDirc = r'C:\Users\gusto\Downloads'
aftDire = r'D:\bigworld\collections\pics_foxdownloads'
Images = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
names = os.listdir(preDirc)
for name in names:
    if len(name.split('.')) == 2:
        if name.split('.')[1].upper() in Images:
            old_dir = preDirc + '\\' + name
            new_dir = aftDire + '\\' + name
            shutil.move(old_dir, new_dir)
