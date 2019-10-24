#!/usr/bin/env python

import os
import sys
import time
import requests

"""
Usage:
wallpaper.py             # random choose a image from BING_IMAGE_DIR set as wallpaper 
wallpaper.py timearg # random choose a image from BING_IMAGE_DIR set as wallpaper every duration
wallpaper.py -p=path     # random choose a image from path if path exists image else run wallpaper.py
wallpaper.py -p=path -t=duration # 
wallpaper.py today       # set today's bing image as wallpaper
wallpaper.py image_url   # download and set as wallpaper

"""

BING_IMAGE_DIR = "/home/quan/Pictures/bing_pics"
BING_IMAGE_NAME = time.strftime("%Y-%m-%d", time.localtime()) + ".jpg"
IMAGE_TYPE = ('jpg', 'jpeg', 'png')
DOWNLOAD_DIR = "/home/quan/Pictures/download_by_wallpaper"