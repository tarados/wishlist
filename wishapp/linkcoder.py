import re

a = 'http://www.foxtrot.com.ua/ru/shop/multivarki_redmond_rmc-m251.html  Мультиварка REDMOND RMC-M251 поможет вам воплотить' \
    ' в жизнь самые смелые кулинарные идеи. В ней предусмотрено 10 автоматических программ приготовления разнообразных блюд - ' \
    'Борщ, суп, гарниры, овощное рагу, десерты, тушеное мясо и многое другое. В книге рецептов вы найдете множество интересных ' \
    'вариантов и для ежедневного полезного завтрака, и для праздничного ужина. Приверженцы здорового образа жизни несомненно оценят ' \
    'наличие функции пароварки - в комплекте с REDMOND поставляется контейнер для приготовления на пару. Дети тоже будет в восторге, ' \
    'ведь идеально пропекшийся чизкейк и натуральный йогурт – теперь не проблема.'
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
            # newstr.append(substr.replace('\n', '<br>'))
        else:
            substr = substr.replace('\n', '<br>')
            newstr.append(substr)
    str = ' '.join(newstr)
    return str, href, newstr


print(link_on(a)[0])