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

url_origen = 'https://www.agelectronica.com/?n=CODIGO%20ABIERTO,KIT%20ARDUINO&r=0&v=1&pro=1'

TAG = 'CODIGO%20ABIERTO,KIT%20ARDUINO'
URL_SINGLE = f'https://www.agelectronica.com/?n={TAG}&r=0&v=1&pro=1'

page = requests.get(URL_SINGLE)
soup = BeautifulSoup(page.content, 'html.parser')

def num_paginas(resultados):
    #for resultado in resultados:
    sin_espacios = resultados[0].getText().strip().split()
    print(f' Texto: {sin_espacios}, tipo{type(sin_espacios)}')
    inicio = int(sin_espacios[2])
    fin = int(sin_espacios[4])
    paginas = math.ceil(fin / inicio)

    print(f'{int(inicio)}, {int(fin)} tipo inicio: {type(int(inicio))}')
    return inicio, fin, paginas

resultados = soup.findAll("td", {"align": ["right"]})
inicio, fin, paginas = num_paginas(resultados)

print(f'Numero de paginas: {paginas}')

for numero in range(1, inicio + 1):
    print(f'#####Iteracion: {numero}!#####')
    LINEA_X = soup.find_all(id=f"lineas{numero}")
    tds = LINEA_X[0].findAll("td")

    tam_campos = len(tds)
    #print(f"TDs: {tds} {len(tds)}")
    """ x = 0
    for td in tds:
        print(f"TDs[{x}]: {td} {len(td)}")
        x = x+1 """

    foto = tds[0].img['src']
    print(f"foto: {foto} {len(foto)}")

    clave = tds[1].a.text
    print(f"clave: {clave} {len(clave)}")

    descripcion = tds[2].text.strip()
    print(f"descripcion: {descripcion} {len(descripcion)}")

    if tam_campos <= 10:
        pasos_extra = 0
    else:
        pasos_extra = 2
    ficha_tec = tds[3 + pasos_extra].a['href']
    print(f"ficha_tec: {ficha_tec} {len(ficha_tec)}")

    existencia = tds[5 + pasos_extra].text
    print(f"existencia: {existencia} {len(existencia)}")

    precio = tds[7 + pasos_extra].text
    print(f"precio: {precio} {len(precio)}")