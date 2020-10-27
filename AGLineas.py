from bs4 import BeautifulSoup
import requests, math

url_origen = 'https://www.agelectronica.com/?n=CODIGO%20ABIERTO,KIT%20ARDUINO&r=0&v=1&pro=1'

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

#print(soup.find_all(id="first"))

#print(soup.select("div p"))
#print(soup.find_all(id="lineas1"))

resultados = soup.findAll("td", {"align": ["right"]})
print(f'Numero de paginas: {num_paginas(resultados)}')

lista = [1,2,3]

LINEA_X = soup.find_all(id="lineas2")
print(f"!!!!!!!!!Linea_X: {LINEA_X} {len(LINEA_X)}!!!!!!!!!!!!!!!") #1

tds = LINEA_X[0].findAll("td")

print(f"TDs: {tds} {len(tds)}") #10
x = 0
for td in tds:
    print(f"TDs[{x}]: {td} {len(td)}")
    x = x+1

foto = tds[0].img['src']
print(f"foto: {foto} {len(foto)}")

clave = tds[1].a.text
print(f"clave: {clave} {len(clave)}")

descripcion = tds[2]
print(f"descripcion: {descripcion} {len(descripcion)}")

if len(tds) <= 10:
    pasos_extra = 0
else:
    pasos_extra = 2
ficha_tec = tds[3 + pasos_extra].a['href']
print(f"ficha_tec: {ficha_tec} {len(ficha_tec)}")
#ficha_tec = tds[5].a['href']
#print(f"ficha_tec: {ficha_tec} {len(ficha_tec)}")


#existencia = tds[4].select("table tr td")[0].text
#print(f"existencia: {existencia} {len(existencia)}")
existencia = tds[5 + pasos_extra].text
print(f"existencia: {existencia} {len(existencia)}")
#existencia = tds[7].text
#print(f"existencia: {existencia} {len(existencia)}")

precio = tds[7 + pasos_extra].text
print(f"precio: {precio} {len(precio)}")
#precio = tds[9].text
#print(f"precio: {precio} {len(precio)}")

""" for tds in linea1:
    print(f"Linea: {linea}")
    if linea.td:
        print(f"Linea td: {linea.td}") """


#print(soup.select("#lineas1"))

"""r=0&v=1&pro=1
r=10&v=1&pro=1
r=20&v=1&pro=1
r=30&v=1&pro=1
r=40&v=1&pro=1
r=50&v=1&pro=1
r=60&v=1&pro=1 """