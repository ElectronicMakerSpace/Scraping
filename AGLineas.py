from bs4 import BeautifulSoup
import requests, math

TAG = 'CODIGO%20ABIERTO,KIT%20ARDUINO'

URL_SINGLE = f'https://www.agelectronica.com/?n={TAG}&r=0&v=1&pro=1'
URL_ALL = f'https://www.agelectronica.com/?n={TAG}&r=30&v=1&pro=1'

page = requests.get(URL_SINGLE)
soup = BeautifulSoup(page.content, 'html.parser')

def num_paginas(resultados):
    for resultado in resultados:
        sin_espacios = resultado.getText().strip().split()
        print(f' Texto: {sin_espacios}, tipo{type(sin_espacios)}')
        inicio = int(sin_espacios[2])
        fin = int(sin_espacios[4])
        paginas = math.ceil(fin / inicio)

        print(f'{int(inicio)}, {int(fin)} tipo inicio: {type(int(inicio))}')
    return paginas

#print(soup.prettify())
#print(list(soup.children))

#print(soup.find_all('p', class_='outer-text'))
#print(soup.find_all(class_="outer-text"))

#print(soup.find_all(id="first"))

#print(soup.select("div p"))
#print(soup.find_all(id="lineas1"))

resultados = soup.findAll("td", {"align": ["right"]})

print(f'Numero de paginas: {num_paginas(resultados)}')

tablerow = soup.find_all(id="lineas1")
#print(tablerow)

x = 0
for row in tablerow:
    tds = row.findAll("td")
    x = x + 1
    print(f'{x}: {tds}')
    #print(tag.getText())

print(tds)

for x in range(0,len(tds)):
    print (f'{x}->{tds[x]}')

#print(soup.select("#lineas1"))

"""r=0&v=1&pro=1
r=10&v=1&pro=1
r=20&v=1&pro=1
r=30&v=1&pro=1
r=40&v=1&pro=1
r=50&v=1&pro=1
r=60&v=1&pro=1 """

