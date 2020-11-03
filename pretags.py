from bs4 import BeautifulSoup
import requests, math


"""
div.limiteTABLA table(width="98%") tbody tr td(3) align="right"
div.limiteTABLA table(width="100%") tbody tr(linea)->td
r=0&v=1&pro=1
r=10&v=1&pro=1
r=20&v=1&pro=1
r=30&v=1&pro=1
r=40&v=1&pro=1
r=50&v=1&pro=1
r=60&v=1&pro=1 """

#url_origen = 'https://www.agelectronica.com/?n=CODIGO%20ABIERTO,KIT%20ARDUINO&r=0&v=1&pro=1'

TAG = 'CODIGO%20ABIERTO,KIT%20ARDUINO'
URL_SINGLE = f'https://www.agelectronica.com/?n={TAG}&r=60&v=1&pro=1'
URL_BASURA = f'https://www.agelectronica.com/?n=115164851d5ededefwrfgref4'

page = requests.get(URL_BASURA)
soup = BeautifulSoup(page.content, 'html.parser')

def num_paginas(resultados):
    #for resultado in resultados:
    sin_espacios = resultados[0].getText().strip().split()
    print(f' Texto: {sin_espacios}, tipo{type(sin_espacios)}')
    inicio = int(sin_espacios[2])
    fin = int(sin_espacios[4])
    if inicio or fin <= 0:
        paginas = 0
    else:
        paginas = math.ceil(fin / inicio)

    print(f'{int(inicio)}, {int(fin)} tipo inicio: {type(int(inicio))}')
    return inicio, fin, paginas

resultados = soup.findAll("td", {"align": ["right"]})
inicio, fin, paginas = num_paginas(resultados)

print(f'Numero de paginas: {paginas}')

agresult =  soup.findAll("div", {"id": "result"})

#print(agresult)
print(len(agresult))

tablas = soup.findAll("div", {"class": "limiteTABLA"})

#print(tablas)
print(len(tablas))

#print(tablas[1])

#LINEA_X = tablas[1].findAll(id="lineas1")
#trs = tablas[1]
#print(f'{LINEA_X} {len(LINEA_X)}')

#LINEA_X = tablas[1].findChildren()
LINEA_X = tablas[1].findAll('tr', {"id": True})
print(f'{len(LINEA_X)}')

#print(f'{LINEA_X[0].tr[0].attrs}')

lineastr = []

for indice, valor in enumerate(LINEA_X):
    atributos = valor.attrs
    #if ['id'] in atributos:
    #    if  'lineas' in atributos['id']:
    #        lineastr.append(valor)
    #print(f'{indice}:atributos: {atributos}')
    if 'style' not in atributos:
        #print(f'{indice}:atributos: {atributos}')
        cadenalinea = atributos['id']
        lineastr.append(cadenalinea)

print(f'{lineastr}, len: {len(lineastr)}')