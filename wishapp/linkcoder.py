import re

str = 'http://127.0.0.1:8000/dreamers/1/ вы http://127.0.0.1:8000/dreamers/1/ явааи' \
      ' http://othervision.info/zayavleniya-rossii-o-sposobnosti-s-400-pobedit-f-35-okazalis-fejkom-the-national-interest/?utm_referrer=https%3A%2F%2Fzen.yandex.com '
print(len(str))
def linkOn(str):
    a = []
    if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d\w+]+', str):
        for c in re.findall(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d\w+]+', str):
            print(c)
            str = str.replace(c, '<a href="' + c + '">' + c + '</a>')
    return str

linkOn(str)