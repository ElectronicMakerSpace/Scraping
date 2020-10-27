from bs4 import BeautifulSoup
import requests, pandas as pd

# Creating list to store scrap data.
product_name = []
product_price = []
product_rating = []

print(len(product_name))
print(len(product_price))
print(len(product_rating))

url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.title.text) # para testear que funciona

containers = soup.find_all('a',class_ = '_31qSD5')
#print(type(containers))
#print(containers[0]) #el primer a de la lista con clase _31qSD5

for container in containers:
	name = container.find('div',class_ = '_3wU53n')
	product_name.append(name.text)
 
	price = container.find('div',class_ = '_2rQ-NK')
	product_price.append(price.text)
 
	rating = container.find('div', class_ = 'hGSR34')
	product_rating.append(float(rating.text))

print(len(product_name))
print(len(product_price))
print(len(product_rating))

# creating a data frame ...
product_dict = {'Name':product_name,
		'Price':product_price,
		'Rating':product_rating}

df = pd.DataFrame(product_dict)
#print(df)
try:
	df.to_excel(r'flipkart_data.xlsx',index=False)
except Exception as e:
	print(e)