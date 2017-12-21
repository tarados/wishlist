import re


def link_on(str):
    newstr = []
    str = str.split(' ')
    for substr in str:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr):
            c = re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+_(),]+', substr).group()
            b = '<a href="' + c + '">' + c[:20] + '...' + '</a>'
            substr = substr.replace(c, b)
            newstr.append(substr.replace('\n', '<br>'))
        else:
            substr = substr.replace('\n', '<br>')
            newstr.append(substr)
    str = ' '.join(newstr)
    return str

