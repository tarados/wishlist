import re

str = 'http://127.0.0.1:8000/dreamers/1/ вы https://metanit.com/web/javascript/6.1.php явааи' \
      ' http://othervision.info/zayavleniya-rossii-o-sposobnosti-s-400-pobedit-f-35-okazalis-fejkom-the-national-interest/?utm_referrer=https%3A%2F%2Fzen.yandex.com '
abc = 'http://127.0.0.1:8000/dreamers/1/ dlkfj https://webformyself.com/ fghjdfg https://www.8host.com/blog/cikly-for-v-python-3/ ytoouo '

def linkOn(str):
    if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
        for c in re.findall(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
            b = '<a href="' + c + '">' + c + '</a>'
            str = str.replace(c, b)
    return str

linkOn(str)