"""
origin:
https://github.com/geekcomputers/Python/blob/master/Organise.py
"""
import os
import sys
import shutil


EXT_IMAGE_LIST = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
EXT_DOCUMENT_LIST = [
    'DOC',
    'DOCX',
    'PPT',
    'PPTX',
    'PAGES',
    'PDF',
    'ODT',
    'ODP',
    'XLSX',
    'XLS',
    'ODS',
    'TXT',
    'IN',
    'OUT',
    'MD']

try:
    oldDir = sys.argv[1]
    newDir = sys.argv[2]
except BaseException:
    pass


def moveImages(oldDir, newDir):
    lst = os.listdir(oldDir)
    for file in lst:
        try:
            if file.split('.')[1].upper() in EXT_IMAGE_LIST:
                shutil.move(oldDir + '\\' + file, newDir)
        except BaseException:
            pass


if __name__ == "__main__":
    moveImages(oldDir, newDir)
