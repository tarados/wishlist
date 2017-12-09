import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
# URL = 'https://calls.su/catalog/kompyutery-i-periferiya/kabeli-shlejfy-i-perekhodniki/kabeli/kabel-soedinitelnyy-dexp-usb-a-usb-b/'
# URL = 'https://hard.rozetka.com.ua/ua/samsung_mz_v6e500bw/p15359221/'
# URL = 'http://teza.shop/catalog/torgovoe-oborudovanie/biryusa-200n-5'

def get_img(url):
    response = requests.get(url, headers=headers)
    data = response.text
    begin = data.find('og:image', 0, len(data))
    end = data.find('>', begin, len(data))
    img_data = data[begin:end]
    # print(img_data)
    # print(begin)
    # print(end)
    if begin > 0:
        img_url_begin = img_data.find('http', 0, len(img_data))
        img_url_end = img_data.find('jpg', 0, len(img_data))
        if img_url_begin > 0:
            result = img_data[img_url_begin:img_url_end + 3]
            return result
        else:
            url_domen = url.split('/')[0] + '//' + url.split('/')[2]
            result = url_domen + img_data[img_data.find('/'):img_data.find('jpg') + 3]
            return result
    else:
        result = '/static/img/new_year.png'
        return result

# print(get_img(URL))

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
