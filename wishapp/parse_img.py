import requests
from bs4 import BeautifulSoup
import re


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
a = 'https://megamag.online/catalog/gazonokosilki/gazonokosilka-rotornaya-bosch-arm-34-06008a6101/'

def get_img(url):
    try:
        response = requests.get(url, headers=headers)
        data = response.text
        if len(data) < 1000:
            response = requests.get(url, headers=headers)
            data = response.text
        url_domen = url.split('/')[0] + '//' + url.split('/')[2] + '/'
        # print(url_domen)
        soup = BeautifulSoup(data,'html.parser')
# проверяем тег meta
        result_meta = ''
        try:
            p = re.compile('og:image')
            for s in soup.find_all(property=p):
                if len(s['property']) == 8:
                    if s['content'].find('http') + 1 > 0:
                        result_meta = s['content']
                    else:
                        result_meta = url_domen + s['content']
            # print(result_meta)
        except:
            pass
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
    except:
        result_meta = None
        result_img = None
        result_a = None
# выбираем из трех 1-2-3
#     print(result_img)
#     print(result_meta)
#     print(result_a)
    result = None
    if result_meta != '':
        result = result_meta
    else:
        if result_img != '':
            result = result_img
        else:
            if result_a != '':
                result = result_a
    return result

print(get_img(a))


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
        soup = BeautifulSoup(data,'html.parser')
        title = soup.find('h1').text
    else:
        title = ''
    return title
