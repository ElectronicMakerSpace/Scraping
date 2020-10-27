import urllib.request

def download_file(url):
    nombre_local_imagen = "prueba.jpg" # El nombre con el que queremos guardarla
    urllib.request.urlretrieve(url, nombre_local_imagen)

if __name__ == '__main__':
    url = 'https://agelectronica.com/FOTOS/O/OKY2007-1.jpg'
    download_file(url)