import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

def get_img(url):
    response = requests.get(url, headers=headers)
    data = response.text
    url_domen = url.split('/')[0] + '//' + url.split('/')[2]
    soup = BeautifulSoup(data,'html.parser')
# проверяем тег meta
    try:
        meta = soup.find('meta', property="og:image")['content']
        if meta.find('http') + 1 > 0:
            result_meta = meta
        else:
            result_meta = url_domen + meta
    except:
        result_meta = None
# проверяем тег а
    result_a = None
    for a in soup.find_all('a'):
        try:
            if a['href'].find('.jpg') > 0:
                if a['href'].find('http') + 1 > 0:
                    result_a = a['href']
                else:
                    result_a = url_domen + a['href']
        except:
            pass
        try:
            if a['href'].find('.png') > 0:
                if a['href'].find('http') + 1 > 0:
                    result_a = a['href']
                else:
                    result_a = url_domen + a['href']
        except:
            pass
# проверяем тег img
    for img in soup.find_all('img'):
        try:
            if img['src'].find('.jpg') > 0:
                if img['src'].find('http') + 1 > 0:
                    result_img = img['src']
                else:
                    result_img = url_domen + img['src']
        except:
            pass
        try:
            if img['src'].find('.png') > 0:
                if img['src'].find('http') + 1 > 0:
                    result_img = img['src']
                else:
                    result_img = url_domen + img['src']
        except:
            pass
# выбираем из трех 1-2-3
    if result_meta != None:
        result = result_meta
    else:
        if result_a != None:
            result = result_a
        else:
            if result_img != None:
                result = result_img
# и если изображения все равно нет, устанавливаем значение по умолчанию
    if result == None:
        result = '/static/img/new_year.png'
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
    return url[0]
