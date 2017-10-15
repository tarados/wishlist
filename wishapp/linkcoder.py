import re

a = 'test http://google.com sdsaasddds dfgsdgdbasdg http://google.com/?q=1 http://google.com/?q=samsung dd http://google.com/?q=samsung'
d = 'test http://google.com/?q=1 sdsaasddds dfgsdgdbasdg http://google.com http://google.com/?q=samsung dd http://google.com/?q=samsung'

def linkOn(str):
    if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
        for c in re.findall(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%\d+\w+]+', str):
            print(c)
            b = '<a href="' + c + '">' + c + '</a>'
            print(b)
            str = str.replace(c, b)
    return str

print(linkOn(d))