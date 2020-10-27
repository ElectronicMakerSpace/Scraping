# scraping a static website ..
from bs4 import BeautifulSoup
import requests
data = requests.get('http://quotes.toscrape.com/')
#print(data)
#print(data.status_code)

soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify()) #se imprime todo el html
#print(soup.title) #<title>Quotes to Scrape</title>
#print(soup.title.text) #Quotes to Scrape

#anchor = soup.find_all('a') # creal una lista con todas las tags [a, a, a, ... an]
#print(anchor)

#regresar la primer coincidencia de una etiqueta a 
#anchor = soup.find('a').get_text()
anchor = soup.find_all('a')[0].get_text()
print(anchor)

#busqueda por span con class="text"
#busqueda por id soup.find_all(id="first")
quote1 = soup.find_all('span', class_ ="text")[0].get_text()
print(quote1)

"""
 Here are some examples:

⦁ p a — finds all a tags inside of a p tag.
⦁ body p a — finds all a tags inside of a p tag inside of a body tag.
⦁ html body — finds all body tags inside of an html tag.
⦁ p.class_name— finds all p tags with a class of class_name.
⦁ p#first — finds all p tags with an id of first.
⦁ body p.class_name— finds any p tags with a class of class_name inside of a body tag.
"""
# Se cre una lista con todos los a dentro de un span que estan dentro de un div
css_data = soup.select('div span a')
print(css_data) 
