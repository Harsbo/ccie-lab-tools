#!/usr/bin/env python

"""
Put this script in /opt/unetlab/addons/qemu and run against your
file/web server where you store network device images to use with EVE-NG

Prereqs: apt-get install python-pip && pip install wget bs4 requests
"""

import os
import requests
import wget
from bs4 import BeautifulSoup

selected_images = []

def list_directory(url):
    page = requests.get(url).text
    directories = [url + node.get('href') for node in BeautifulSoup(page, 'html.parser').find_all('a') if node.get('href').endswith('/')]
    directories = [x for x in directories if not x.endswith('../')]
    return directories

def list_files(url):
    page = requests.get(url).text
    files = [url + node.get('href') for node in BeautifulSoup(page, 'html.parser').find_all('a') if node.get('href')]
    files = [x for x in files if not x.endswith('../')]
    return files

def select_images(url):
    print(' ')
    for image_dir in list_directory(url):
        image_name = image_dir[len(url):].strip('/')
        print('Download: ' + image_name + ' ')
        if raw_input("y/n? ") == 'y':
            selected_images.append(image_name)

def download_image(image, url):
    if not os.path.exists(image):
        os.makedirs(image)
    for file in list_files(url + image + '/'):
        print('\nDownloading ' + file)
        if not os.path.exists(file[len(url):]):
            wget.download(file, out=file[len(url):])
            print(' ')
        else:
            print('File already exists, skipping. ')

def main():
    URL = raw_input("\nHTTP/HTTPS URL for EVE images directory (don't forget trailing /!): ")
    try:
        select_images(URL)
        print(' ')
    except:
        print('Not a working/reachable URL')
        exit()
    for image in selected_images:
        download_image(image, URL)
    print('\nFix the file permissions:')
    print('/opt/unetlab/wrappers/unl_wrapper -a fixpermissions\n')


if __name__ == "__main__":
    if os.getcwd() == '/opt/unetlab/addons/qemu':
        main()
    else:
        print('This script should be executed in /opt/unetlab/addons/qemu')
