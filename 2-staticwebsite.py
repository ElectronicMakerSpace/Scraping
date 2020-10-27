# scraping a static website ..
from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(data.content, 'html.parser')

# scraping data ..
quote_data = soup.find_all('span',class_ ='text')
author_data = soup.find_all('small', class_ = 'author')
tags_data =  soup.find_all('div' ,class_="tags")

# Extracting text ...
quote = [q.get_text() for q in quote_data]
author = [a.get_text() for a in author_data]
tags = [t.get_text().replace('\n','').replace('Tags:','') for t in tags_data]

# first convert data into dictionary and then dictionary into EXcel file .
data_dict = {'Author':author,
			'Quote':quote,
			'Tags':tags}
# convert dicionary into dataframe.
df = pd.DataFrame(data_dict)
# convert dataframe into Excel file.
df.to_excel(r'scrap_data.xlsx',index=False)