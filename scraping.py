# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
	Web scraping demo. 

	Note: make sure to create a virtualenv and run(if you haven't done so):
		$ pip install -r requirements.txt
	
	This demo uses the following libraries:
		- requests
		- BeautifulSoup

	We will scrape the front page of Hacker News, collect all the 
	links and their text and output them in our very own HTML file. 

	
	© 2017 Vikram Bahl
'''

import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/'

def storeLinksToHTMLFile(allHeadlines):
	
	#the htmlString variable will contain the list of links and the link text
	htmlString = ""

	for link in allHeadlines:
		htmlString += "<a href={}>{}</a><br>".format(link["href"].encode('utf-8'), link.text.encode('utf-8'))
		
	with open("test.html", 'w+') as f:
		f.write(htmlString)

def scrape_N_pages(url, N):
	#make a GET request & grab the HTML text
	request = requests.get(url)
	html = request.text

	#Iniitialise bs4 with html.parser
	soup = BeautifulSoup(html, 'html.parser')
	
	headlines = soup.find_all(attrs={"class":"storylink"})

	#find the <a> selector with class "morelink". Make sure that you know if there is more than one element with the class "morelink"...
	#...and improvise accordingly.
	nextlink = soup.find_all(attrs={"class":"morelink"})
	#as of March '17, there is only once selector with the class "morelink"
	next_resource = nextlink[0]
	
	for link in headlines:
		print link.text
	
	#grab the last character of news?p=2 and check if its not greater than N
	if int((next_resource["href"])[-1]) > N:
		return
	new_url = URL + next_resource["href"]
	#recurse away. beware of stack overflow!!
	scrape_N_pages(new_url)


def get_all_links():
	#make a GET request & grab the HTML text
	request = requests.get(URL)
	html = request.text

	#Iniitialise bs4 with html.parser
	soup = BeautifulSoup(html, 'html.parser')

	'''
		Now we are going to learn some basics of the  BeautifulSoup library.
		The best way to get the gist is to go through the quickstart:
			https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

	'''

	#the prettify() function de-minifies the HTML and nests the tags in a visually appealing manner.
	#do note that depending on the webpage, the prettify() command may take some time to complete.
	print soup.prettify()

	#prints the <title> element
	print "<title> element\n"
	print soup.title
	print "\n--------------------\n"

	#print the first <a> element
	print "<a> element\n"
	print soup.a
	print "\n--------------------\n"

	#prints the first tr element
	print "<tr> element\n"
	print soup.tr
	print "\n--------------------\n"

	#prints the first <form> element
	print "<form> element\n"
	print soup.form
	print "\n--------------------\n"

	'''
	This is fine and well. But usually we will want to scrape a webpage for  the links or 
	all the images or a subset of all images having a particular id or belonging to a particular class.

	And so this is what we will do. Lets scrape the front page of hacker news and grab the all links which
	are headlines and the headline text.
	'''

	#the find_all() function gets all elements with a certain tag or attributes. 
	#check out this link for all filters: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree

	#return a list of all <a>
	print "LIST OF ALL <a> tags in the soup"
	print soup.find_all('a')
	print "\n--------------------\n"

	'''
		But we dont really want ALL links. we want links which point to a headline on the front page.
		This is where am hoping you know how to use the developer tools on your browser('Inspect' in Google Chrome). 
		Basically, the links which point to a headline all belong to the class 'storylink'. 
		The find_all(attrs={"class":"storylink"}) will do that for us.

	 '''

	print "LIST OF ALL <a> tags pointing to a headline"
	allHeadlines = soup.find_all(attrs={"class":"storylink"})
	print allHeadlines
	print "\n--------------------\n"

	#lets see what is the class type of a link from this soup
	print type(soup.find('a'))
	print "\n--------------------\n"

	#It is a <class 'bs4.element.Tag'>. Hmm that's NOT a string. We extract the url and text from the headline by accessing
	#the href attribute and text attribute using link['href'] and link.text

	for link in allHeadlines:
		print "{}\n{}\n\n".format(link.text.encode('utf-8'), link["href"].encode('utf-8'))

	#you can go one step further and store all scraped results in your own HTML file. the possibilities are endless. 
	#Uncomment below to see store all links to HTML file
	#storeLinksToHTMLFile(allHeadlines)

	

if __name__ == '__main__':
	#starting point
	get_all_links()

	"""
		Uncomment below to see run the code which scrapes the first 10 pages of HN headlines.
		Trick: Finding out the class of the "More" link, grabbing the relative url, appending it to the base url and using recursion to scrape N
		pages. But when to stop scraping? Luckily, the relative url of the "More" link is structured as "news?p=2", where 2 is a reference to get the 2nd page
	"""
	#scrape_N_pages(URL, 10)
