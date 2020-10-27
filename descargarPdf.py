import requests

url = 'https://agelectronica.lat/pdfs/textos/O/OKY2002111111111-1.PDF'

response = requests.get(url, stream=True)
num = response.status_code

if num == 200:
    with open('unpdf.pdf', 'wb') as f:
        f.write(response.content)
else:
    print("url invalida")