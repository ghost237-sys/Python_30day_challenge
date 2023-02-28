#this is the project from where i learned web scraping....youtube channel tech with tim
#navigating the html tree
#we trying to find the prices of different crypto currencies from a site

from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result,'html.parser')

tbody = doc.tbody #acccesing the tbody tag

trs = tbody.contents  #gives the tags inside the tbody tag


prices = {}

for tr in trs[:10]:#for those after the index 10...theree was an error and its easier this way..
	name,price =  tr.contents[2:4]:#the indexing in order to get the name and price....skip the icons and stuff
		#we use the p tag because the name of the currency is ther
		fixed_name = name.p.string
		fixed_price = price.a.string

		prices[fixed_name] = fixed_price

print(prices)




