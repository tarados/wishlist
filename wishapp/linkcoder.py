import re

a = 'http://www.foxtrot.com.ua/ru/shop/multivarki_redmond_rmc-m251.html dfghadf'
def link_on(str):
    newstr = []
    href = '/static/img/new_year.png'
    str = str.split(' ')
    for substr in str:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr):
            c = re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr).group()
            href = c
            b = '<a href="' + c + '">' + c[:20] + '...' + '</a>'
            substr = substr.replace(c, b)
            newstr.append(substr.replace('\n', '<br>'))
        else:
            substr = substr.replace('\n', '<br>')
            newstr.append(substr)
    str = ' '.join(newstr)
    return str, href, substr


print(link_on(a)[2])