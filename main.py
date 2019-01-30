# -*- coding: utf-8-sig-*-
import requests
from bs4 import BeautifulSoup
import os


def get_html(url):
    r = requests.get(url)
    return r.text


def get_url_images(text):
    urls = []
    soup = BeautifulSoup(text, 'lxml')
    abc = soup.find_all('div', class_="interior_item")
    for ab in abc:
        img = 'https://art-oboi.com.ua' + ab.find('div', class_="interior_item_box").find('img').get('data-original')
        urls.append(img)
    return urls


def get_file(url):
    r = requests.get(url, stream = True)
    return r


def get_name(url):
    name = url.split('/')[-1]
    folder = name.split('.')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    return path + '/' + name


def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


def main():
    url = 'https://art-oboi.com.ua/photooboi-interior'
    urls = get_url_images(get_html(url))
    for url in urls:
        save_image(get_name(url), get_file(url))


if __name__ =='__main__':
    main()