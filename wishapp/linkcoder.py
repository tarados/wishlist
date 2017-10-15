import re

str = 'test http://google.com sdsaasddds\n dfgsdgdbasdg http://google.com/?q=1\n http://google.com/?q=samsung\n dd http://google.com/?q=samsung'
def linkOn(str):
    newstr = []
    str = str.split(' ')
    for substr in str:
        if re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+]+', substr):
            c = re.search(r'[Hh-sS]\w+:[//.aA-zZ:\-?&=%#\d+\w+]+', substr).group()
            b = '<a href="' + c + '">' + c + '</a>'
            substr = substr.replace(c, b)
            newstr.append(substr.replace('\n', '<br>'))
        else:
            substr = substr.replace('\n', '<br>')
            newstr.append(substr)
    str = ' '.join(newstr)
    # if re.search(r'\n', str):
   # str = str.replace('\n', '<br>')
    return str

print(linkOn(str))