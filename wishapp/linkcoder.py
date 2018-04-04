import re
from wishapp.parse_img import get_img

a = 'dfsdfs'


def link_on(str):
    text = []
    href_list = []
    href_link = '#'
    href_img = '#'
    str_desire = str.split(' ')
    for substr in str_desire:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr):
            href_list.append(re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr).group())
        else:
            substr = substr.replace('\n', '<br>')
            text.append(substr)
    text_desire = ' '.join(text)
    if len(href_list) != 0:
        for href in href_list:
            if re.search(r'.jpg|.png', href):
                href_img = href
            else:
                href_link = href
    return text_desire, href_link, href_img


# link_on(a)
# print(link_on(a)[0])
# print(link_on(a)[1])
# print(link_on(a)[2])
