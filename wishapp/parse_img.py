import requests
from bs4 import BeautifulSoup
import re


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}


def get_img(url):
    response = requests.get(url, headers=headers)
    data = response.text
    url_domen = url.split('/')[0] + '//' + url.split('/')[2] + '/'
    soup = BeautifulSoup(data,'html.parser')
# проверяем тег meta
    try:
        meta = soup.find('meta', property="og:image")['content']
        if meta.find('http') + 1 > 0:
            result_meta = meta
        else:
            result_meta = url_domen + meta
    except:
        result_meta = ''
# проверяем тег а
    result_a = ''
    href = re.compile(r'\.jpg')
    try:
        a = soup.find('a', href=href)
        if a['href'].find('http') + 1 > 0:
            result_a = a['href']
        else:
            result_a = url_domen + a['href']
    except:
        pass
# проверяем тег img
    result_img = ''
    src = re.compile(r'[^index]\.jpg')
    try:
        img = soup.find('img', src=src, title=True)
        if img['src'].find('http') + 1 > 0:
            result_img = img['src']
        else:
            result_img = url_domen + img['src']
    except:
        pass
    if result_img == '':
        try:
            img = soup.find('img', src=src)
            if img['src'].find('http') + 1 > 0:
                result_img = img['src']
            else:
                result_img = url_domen + img['src']
        except:

            pass
# выбираем из трех 1-2-3
    result = '/static/img/new_year.png'
    if result_meta != '':
        result = result_meta
    else:
        if result_img != '':
            result = result_img
        else:
            if result_a != '':
                result = result_a
    return result


def find_url(str):
    d = str.find('http') + 1
    is_url = d > 0
    return is_url


def get_url(str):
    url = []
    for d in str.split(' '):
        if d.find('http') + 1:
            url.append(d)
        else:
            url.append('/static/img/new_year.png')
    return url[0]


def get_title(url):
    if url != '/static/img/new_year.png':
        response = requests.get(url, headers=headers)
        data = response.text
        url_domen = url.split('/')[0] + '//' + url.split('/')[2] + '/'
        soup = BeautifulSoup(data,'html.parser')
        title = soup.find('h1').text
    else:
        title = 'noname'
    return title
