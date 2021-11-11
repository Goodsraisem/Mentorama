from requests import get
from bs4 import BeautifulSoup

x = get("https://pt.wikipedia.org/wiki/Vergil")
tags = BeautifulSoup(x.text,"html5lib")
principal = tags.find('h1', attrs= { })
secundarias = tags.find_all('a', href=True, title=True)
sec = [a.text for a in secundarias]


print("Página Principal:", principal.text)
for i in sec:
    print("Página Secundaria:", i)
