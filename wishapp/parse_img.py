import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

def get_img(url):
    response = requests.get(url, headers=headers)
    data = response.text
    url_domen = url.split('/')[0] + '//' + url.split('/')[2]
    begin = data.find('og:image', 0, len(data))
    end = data.find('>', begin, len(data))
    img_data = data[begin:end]
    if begin > 0:
        img_url_begin = img_data.find('http', 0, len(img_data))
        img_url_end = img_data.find('jpg', 0, len(img_data))
        if img_url_begin > 0:
            result = img_data[img_url_begin:img_url_end + 3]
            return result
        else:
            result = url_domen + img_data[img_data.find('/'):img_data.find('jpg') + 3]
            return result
    else:
        result = ''
        soup = BeautifulSoup(data, 'html.parser')
        for a in soup.find_all('a'):
            try:
                b = a['href'].find('.jpg')
                if b > 0:
                    result = url_domen + a['href']
                    return result
            except:
                pass
        if result == '':
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
