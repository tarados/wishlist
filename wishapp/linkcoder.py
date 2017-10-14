import re

def linkOn(str):
    if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
        for c in re.findall(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
            b = '<a href="' + c + '">' + c + '</a>'
            str = str.replace(c, b)
    return str
