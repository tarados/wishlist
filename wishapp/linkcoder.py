import re


def linkOn(str):
    newstr = []
    str = str.split(' ')
    for substr in str:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+]+', substr):
            c = re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+]+', substr).group()
            b = '<a href="' + c + '">' + c + '</a>'
            newstr.append(b)
        else:
            newstr.append(substr)
    str = ' '.join(newstr)
    return str

