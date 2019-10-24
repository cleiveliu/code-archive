import os
import shutil


def move(olddir, newdir):
    """
    move undamaged music from old dirctory to new directory.
    """
    musics = os.listdir(olddir)
    already = os.listdir(newdir)
    wanted_music = ['flac', 'ape', 'wav']
    for music in musics:
        try:
            if music not in already:
                if music.lower().split('.')[1] in wanted_music:

                    shutil.copy(olddir + "\\" + music, newdir)
        except BaseException:
            pass
    print("DONE")


if __name__ == '__main__':
    move(r'D:\bigworld\CloudMusic', 'D:\\new')
