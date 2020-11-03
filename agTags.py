from bs4 import BeautifulSoup
import requests, math

url_origen = 'https://www.agelectronica.com/?n=CODIGO%20ABIERTO,KIT%20ARDUINO&r=0&v=1&pro=1'
TAG = 'CODIGO%20ABIERTO,KIT%20ARDUINO'
pagina = 0
URL_SINGLE = f'https://www.agelectronica.com/?n={TAG}&r={pagina}&v=1&pro=1'
URL_BASURA = f'https://www.agelectronica.com/?n=testderesultados'

paginaInicio = requests.get(URL_SINGLE)
soup = BeautifulSoup(paginaInicio.content, 'html.parser')

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

if paginas < 1:
    print('No hay paginas que inspeccionar')
if paginas >= 1:
    URL_COMPUESTA = f'https://www.agelectronica.com/?n={TAG}&r={pagina}&v=1&pro=1'
    
    paginaIterable = requests.get(URL_COMPUESTA)
    soup = BeautifulSoup(paginaIterable.content, 'html.parser')
    
    agresult =  soup.findAll("div", {"id": "result"})
    print(len(agresult))

    tablas = soup.findAll("div", {"class": "limiteTABLA"})
    print(len(tablas))

    LINEA_X = tablas[1].findAll('tr', {"id": True})
    print(f'{len(LINEA_X)}')

    lineastr = []

    for indice, valor in enumerate(LINEA_X):
        atributos = valor.attrs
        if 'style' not in atributos:
            cadenalinea = atributos['id']
            lineastr.append(cadenalinea)

    print(f'{lineastr}, len: {len(lineastr)}')

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