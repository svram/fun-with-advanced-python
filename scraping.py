# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
	Web scraping demo. 

	Note: make sure to create a virtualenv and run:
		$ pip install -r requirements.txt
	
	This demo uses the requests and BeautifulSoup libraries

	We will scrape the front page of Hacker News, collect all the 
	links and their text and output them in our very own HTML file. 

	Usage: 
	
	© 2017 Vikram Bahl
'''

import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/'

def test_scraping():
	request = requests.get(URL)
	html = request.text
	soup = BeautifulSoup(html, 'html.parser')
	htmlString = ""
	for link in soup.find_all(attrs={"class":"storylink"}):
		#print type(link["href"])
		htmlString += "<a href={}>{}</a><br>".format(link["href"].encode('utf-8'), link.text.encode('utf-8'))
		#print link.text
		#print link["href"]
	#print htmlString
	with open("test.html", 'w+') as f:
		f.write(htmlString)

def get_all_links():
	#make a GET request & grab the HTML text
	request = requests.get(URL)
	html = request.text

	#Iniitialise bs4 with html.parser
	soup = BeautifulSoup(html, 'html.parser')
	
	#the htmlString variable will contain the list of links and the link text
	htmlString = ""

	'''
		Now we are going to learn some basics of the  BeautifulSoup library.
		The best way to get the gist is to go through the quickstart:
			https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

	'''

	#the prettify() function de-minifies the HTML and nests the tags in a visually appealing manner.
	#do note that depending on the webpage, the prettify() command may take some time to complete.
	print soup.prettify()

	#prints the <title> element
	print soup.title
	#print the first <a> element
	print soup.a
	#prints the first h1 element
	print soup.h1
	#prints the first <form> element
	print soup.form

	





if __name__ == '__main__':
	#test_scraping()
	get_all_links()