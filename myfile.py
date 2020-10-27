from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.python.org/")
    #html = urlopen('https://www.agelectronica.com')

except HTTPError as e:
    print(e)

except URLError:
    print("Server down or incorrect domain")

else:
    res = BeautifulSoup(html.read(),"html5lib")
    
    # todas las h2 con clase widget-title
    #tags = res.findAll("h2", {"class": "widget-title"})
    
    #todas las etiquetas span, a e img
    #tags = res.findAll("span", "a" "img")
    #tags = res.findAll("a", {"class": ["url", "readmorebtn"]})
    #tags = res.findAll(text="All the Flow You’d Expect")
    
    #Esta línea obtendrá el primer elemento span en el objeto Beautiful Soup y luego obtendrá todos los elementos a en ese span.
    tags = res.findAll("a")

    #tag = res.find("nav", {"id": "site-navigation"}).select("a")[3]
    
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title)

    #print(tag)

    for tag in tags:
        #print(tag)
        print(tag.getText())