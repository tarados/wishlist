import re
import random
import string


def link_on(str):
    text = []
    href_list = []
    href_link = '#'
    href_img = '#'
    str_desire = str.split(' ')
    for substr in str_desire:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),*]+', substr):
            href_list.append(re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),*]+', substr).group())
        else:
            substr = substr.replace('\n', '<br>')
            text.append(substr)
    text_desire = ' '.join(text)
    if len(href_list) != 0:
        for href in href_list:
            if re.search(r'.jpg|.png', href):
                href_img = href
            elif re.search(r'.jpeg', href):
                href_img = href
            else:
                href_link = href
    return text_desire, href_link, href_img


def substitute_id():
    sub_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return sub_id


