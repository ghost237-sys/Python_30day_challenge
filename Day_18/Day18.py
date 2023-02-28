#web scraping using python 
#for this we are using the module beautifulsoup
from bs4 import BeautifulSoup

with open('index.html','r') as f:
	doc = BeautifulSoup(f,'html.parser')
#print(doc.prettify())#prints out the html file as a text...the prettify enables indentation making it look better and more organized


#finding by tags
tag = doc.title
print(tag.string)#we use the .string to acces the string inside the tag
#output is your title here
#change the value in the tag
tag.string = 'hello'
print(tag.string)#the tag now is hello...displays hello

tag = doc.find('a')#displays the first a tag
print(tag.string)

tags= doc.find_all('a')#displays all a tags
print(tags.string)

tags = doc.find_all('p')[0]#just like in list indexing
print(tags.find_all('b'))#displays all the b tags in the first p tag


#reading html files from websites
import requests
url = 'www.youtube.com'
result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')
print(doc.prettify())

#for the examples here am using the second html file index2.html
with open('index2.html','r') as fp:
	doc = BeautifulSoup(f,'html.parser')
tag = doc.find('option')
tag['selected'] = 'false'#we can access tags like python dictionaries
print(tag)#displays <option selected="false" value="course-type">Course type*</option>...the selected tag has been changed


#adding attributes
tag['color'] = 'blue'  # a new tag color with value blue is created

#finding more than one tag...by passing a list of the tags you want as arguments
tags = doc.find_all(['option','color','value'])

#finding specific text or values in tags
tags = doc.find_all(['option'],text='undergraduate')#displays the tag with the text undergraduate
tags = doc.find_all(['option'],value='undergraduate')#this is the same as the line above
print(tags)

#looking for different class names
tags = doc.find_all(class_='btn-item')#notice how we use the underscore after class because its a python special name
print(tags)#all the tags that have btn-item as one of their classes

#using regular expressions
import re
with open('index2.html','r') as fp:
	doc = BeautifulSoup(f,'html.parser')

tags = doc.find_all(text=re.compile('\$.*'))
print(tags)#displays all the lines with a dolar sign before them 
#to remove the whitespaces we do
for tag in tags:
	print(tag.strip())

#you can use limit to limit the number of results in a find_all
tags = doc.find_all(text=re.compile('\$.*'),limit=1)#gives out one type

#saving a modified html txt
import re
with open('index2.html','r') as fp:
	doc = BeautifulSoup(f,'html.parser')
	
tags = doc.find_all('input',type='text')
for tag in tags:
	tag['placeholder'] = 'i changed you'

with open('changed.html','w') as file:
	file.write(str(doc))

#this is just a basic intro...you can learn more about the BeautifulSoup module in its documentation