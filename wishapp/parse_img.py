import requests
from bs4 import BeautifulSoup
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
# a = 'https://images.g2a.com/newlayout/323x433/1x1x0/f33820499db3/5911b0d3ae653a3da06fbd97'
# a = 'https://rozetka.com.ua/kids_boys_shoes/c721669/'


# a = 'https://avatars.mds.yandex.net/get-zen_doc/173924/pub_5c078623adc1e400aa856e09_5c078d6223ea6500adc59563/scale_600'

def get_img(url):
    try:
        response = requests.get(url, headers=headers)
        data = response.text
        if len(data) < 1000:
            response = requests.get(url, headers=headers)
            data = response.text
        url_domen = url.split('/')[0] + '//' + url.split('/')[2] + '/'
        # print(url_domen)
        # проверяем Content-type
        result_header = None
        if response.headers.get('Content-Type').split(';')[0] != 'text/html':
            result_header = url
        soup = BeautifulSoup(data, 'html.parser')
        # проверяем тег meta
        result_meta = ''
        meta_list = []
        try:
            p = re.compile('og:image')
            for s in soup.find_all(property=p):
                if s['content'].find('http') + 1 > 0:
                    meta_list.append(s['content'])
                else:
                    meta_list.append(url_domen + s['content'])
            result_meta = meta_list[0]
        except:
            pass
        # проверяем тег а
        result_a = ''
        list_a = []
        href = re.compile(r'\.jpg')
        try:
            for a in soup.findAll('a', href=href):
                if a['href'].find('http') + 1 > 0:
                    result_a = a['href']
                else:
                    if a['href'][1] == '/':
                        list_a.append('https:' + a['href'])
                    else:
                        list_a.append(url_domen + a['href'])
            result_a = list_a[0]
        except:
            pass
        # проверяем тег img
        result_img = ''
        image_list = []
        src = re.compile(r'[^index]\.jpg')
        try:
            for img in soup.findAll('img', alt=re.compile(r'.')):
                if img['src'].find('http') + 1 > 0:
                    image_list.append(img['src'])
                else:
                    image_list.append(url_domen + img['src'])
            result_img = image_list[0]
        except:
            pass
    except:
        result_meta = None
        result_img = None
        result_a = None
    # выбираем из трех 1-2-3
    # print('result_img= ', result_img)
    # print('result_meta= ', result_meta)
    # print('result_a= ', result_a)
    result = None
    if result_meta != '':
        result = result_meta
    else:
        if result_a != '':
            result = result_a
        else:
            if result_img != '':
                result = result_img
    if result_header:
        result = result_header
    return result


# print(get_img(a))


def find_url(str):
    d = str.find('http') + 1
    is_url = d > 0
    return is_url


def get_url(str):
    url = ''
    for d in str.split(' '):
        if d.find('http') + 1:
            url = d
        else:
            pass
    return url


def get_title(url):
    if url != None:
        response = requests.get(url, headers=headers)
        data = response.text
        url_domen = url.split('/')[0] + '//' + url.split('/')[2] + '/'
        soup = BeautifulSoup(data, 'html.parser')
        title = soup.find('h1').text
    else:
        title = ''
    return title
