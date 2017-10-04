import re

a = ['является одним из разносторонних элементов формы и позволяет создавать разные https://habrahabr.ru/post/66931/ dfkjhgdfhgmnvghsn']

b = a[0]
c = re.search(r'[h-s]\w+:[//.\d\w+]+', b).group()
d = b.replace(c, '<a href=' + c + '></a>')
print(d)
print(c)