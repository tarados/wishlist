import requests


def get_img(url):
    response = requests.get(url)
    data = response.text
    begin = data.find('og:image', 0, len(data))
    end = data.find('>', begin, len(data))
    result = data[begin:end].split('"')
    return result[2]
