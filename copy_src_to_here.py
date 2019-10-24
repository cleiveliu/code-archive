

import datetime
import shutil
import os
import threading
SRC_PATH = '/home/quan/Desktop/code'

EXCEPT_DIR = ['.vscode', 'go', '.git']

EXCEPT_EXTENSION = []
EXCEPT_EXTENSION = tuple(EXCEPT_EXTENSION)


current_dir = os.path.split(__file__)[0]

new_dir = os.path.join(current_dir, os.path.split(SRC_PATH)[1])


def gen_legal_abs_path(dir_or_file_name: str, nodirs=EXCEPT_DIR, notypes=EXCEPT_EXTENSION):
    if os.path.exists(dir_or_file_name):
        if os.path.isfile(dir_or_file_name) and not dir_or_file_name.endswith(notypes):
            yield dir_or_file_name
        elif os.path.isdir(dir_or_file_name) and os.path.split(dir_or_file_name)[1] not in nodirs:
            yield dir_or_file_name
            for p in os.listdir(dir_or_file_name):
                abs_dir = os.path.join(dir_or_file_name, p)
                yield from gen_legal_abs_path(abs_dir)


def copy(src=SRC_PATH, des=new_dir):
    if not os.path.exists(des):
        os.mkdir(des)
    file_or_dirs = gen_legal_abs_path(src)
    src_len = len(src)
    for p in file_or_dirs:
        # new_p = os.path.join(des, p[src_len:]) # trans the src abs path to des abs path
        new_p = des + p[src_len:]
        if os.path.isdir(p):
            if not os.path.exists(new_p):
                os.mkdir(new_p)
        elif os.path.isfile(p):
            shutil.copy(p, new_p)


def get_today():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    today = f"{year}{month}{day}"
    return today


def rename_dir(src=new_dir):
    today = get_today()
    new_name = f"{new_dir}-{today}"
    if os.path.exists(new_dir) and not os.path.exists(new_name):
        os.rename(new_dir, new_name)


def format_all_python_files_in_new_dir(des=new_dir):
    files = gen_legal_abs_path(des)
    files = filter(lambda x: os.path.isfile(x) and x.endswith('.py'),
                   files)
    cmd_f = "autopep8 --in-place --aggressive --aggressive {filename}"

    def do_it(cmd):
        os.system(cmd)
    threads = []
    for file in files:
        cmd = cmd_f.format(filename=file)
        t = threading.Thread(target=do_it, args=(cmd, ))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    format_all_python_files_in_new_dir("/home/quan/code/code-archive/code-20191023")
    

# I know this is buggy, I will improve it later
