from bs4 import BeautifulSoup
import requests, math

url_origen = 'https://www.agelectronica.com/?n=CODIGO%20ABIERTO,KIT%20ARDUINO&r=0&v=1&pro=1'
#TAG = 'CODIGO%20ABIERTO,KIT%20ARDUINO'
#TAG = 'PROTECCION,SANITIZANTES,GERMICIDAS'
TAG = 'CODIGO ABIERTO,SENSOR,ORIENTACION'


paginaInit = 0
URL_SINGLE = f'https://www.agelectronica.com/?n={TAG}&r={paginaInit}&v=1&pro=1'
URL_BASURA = f'https://www.agelectronica.com/?n=testderesultados'



paginaInicio = requests.get(URL_SINGLE)
soup = BeautifulSoup(paginaInicio.content, 'html.parser')

def num_paginas(resultados):
    #for resultado in resultados:
    sin_espacios = resultados[0].getText().strip().split()
    print(f' Texto: {sin_espacios}, tipo{type(sin_espacios)}')
    inicio = int(sin_espacios[2])
    fin = int(sin_espacios[4])

    if inicio <=0 or fin <= 0:
        paginas = 0
    else:
        paginas = math.ceil(fin / inicio)

    print(f'{inicio}, {fin} tipo inicio: {type(inicio)}')
    return inicio, fin, paginas

resultados = soup.findAll("td", {"align": ["right"]})
inicio, fin, paginas = num_paginas(resultados)

print(f'Numero de paginas: {paginas}')

if paginas < 1:
    print('No hay paginas que inspeccionar')
if paginas >= 1:
    for pagina in range(paginas):
        print(f'######################### PAGINA: { pagina + 1}!#########################')
        lineastr = []
        URL_COMPUESTA = f'https://www.agelectronica.com/?n={ TAG }&r={ pagina * 10 }&v=1&pro=1'
        paginaIterable = requests.get(URL_COMPUESTA)
        soup = BeautifulSoup(paginaIterable.content, 'html.parser')
        
        agresult =  soup.findAll("div", {"id": "result"})
        #print(len(agresult))

        tablas = soup.findAll("div", {"class": "limiteTABLA"})
        #print(len(tablas))

        trlineas = tablas[1].findAll('tr', {"id": True})
        #print(f'{len(trlineas)}')


        for a in trlineas:
            atributos = a.attrs
            if 'style' not in atributos:
                cadenalinea = atributos['id']
                lineastr.append(cadenalinea)

        #print(f'{lineastr}, len: {len(lineastr)}')

        for idx, linea in enumerate(lineastr):
            print(f'#####Iteracion: {idx + 1}#####')
            LINEA_X = soup.find_all(id=f"{linea}")
            tds = LINEA_X[0].findAll("td")

            tam_campos = len(tds)
            print(f'tam_campos: {tam_campos}')

            fotox = tds[0]
            print(f"fotox: {fotox}")
            foto = tds[0].img['src']
            print(f"foto: {foto}")

            clave = tds[1].a.text
            print(f"clave: {clave}")
    
            descripcion_completa = tds[2].text
            descripcion_ingles = tds[2].findChildren()[0].text.strip()
            result = descripcion_completa.index(descripcion_ingles)

            descripcion_esp = descripcion_completa[:result].strip()
            print(f"descripcion: {descripcion_esp}")

            if tam_campos <= 10:
                pasos_extra = 0
            elif tam_campos == 11:
                pasos_extra = 1
            elif tam_campos == 12:
                pasos_extra = 2
            elif tam_campos == 13:
                pasos_extra = 3
            link = tds[3 + pasos_extra].findChildren()
            atributos = link[0].attrs

            if 'href' in atributos:
                ficha_tec = tds[3 + pasos_extra].a['href']
                print(f"ficha_tec: {ficha_tec}")
            else:
                ficha_tec = "No hay ficha tecnica"
                print(f"ficha_tec: {ficha_tec}")

            existencia = tds[5 + pasos_extra].text
            print(f"existencia: {existencia}")

            precio = tds[7 + pasos_extra].text
            print(f"precio: {precio}")