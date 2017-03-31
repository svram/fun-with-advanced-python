# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
	A word cloud is visual representation of the frequency of words in a corpus 
	with frequency of the word directly proportional to its font size in the representation

	Now the first step in creating the word cloud is to clean the corpus removing
	unnecessary punctuation. The next step is the hard part.

	Does the apostrophe count as punctuation? What if someone uses the word "How's" instead of "How is"
	What about the underscore and the dash?
	Would you treat uppercase, capitalised and lowercase differently?
	How about personal nouns?
	What about a word which is context dependent? Like "Hello Jack" and "This is a jack hammer"

	Depending upon the situation, you would make a decision on the tradeoffs.
	Here are the assumptions we are going with:
		- We will not treat -, _ and ' as punctuation
		- Uppercase words will be converted to lowercase and treated as the same (hello and HELLO will be trated as 2 'hello'-es)
		- Capitalised words will be kept as-is until a lowercase word is found in which case the capitalised word
		  will be converted to lowercase (Jack will remain as such until its lowercase version is found)

	We will be using a dictionary to store our "word:frequency" relationship.

	INPUT: URL of page we want to create a word clud of
	OUTPUT: HTML file with word cloud

	CONSTRAINTS: For now, we will pass the class name of the main block of text we want to make a word cloud of. 
				 In the future, we will get into figuring out which is likely to be the main body of text in an article.
	
	© 2017 Vikram Bahl

'''

from bs4 import BeautifulSoup
import requests

def generate_word_cloud(URL, classname):
	
	mainBodyText = retrieve_main_body_of_text(URL, classname)
	sanitized_text = sanitize_text(mainBodyText)
	word_cloud = create_word_cloud(sanitized_text)

	return word_cloud

def retrieve_main_body_of_text(URL, classname):
	#we extract the text from the page using beautiful soup library.
	#check out the scraping.py file for an intro to beautiful soup

	#make a GET request & grab the HTML text
	request = requests.get(URL)
	html = request.text

	#Iniitialise bs4 with html.parser
	soup = BeautifulSoup(html, 'html.parser')

	#lets grab the main body of text using the classname. Hint: use 'Inspect' in chrome dev tools to do this
	mainBodyText = soup.find_all(attrs={'class': classname})


	return mainBodyText[0].text


def create_word_cloud(corpus):
	pass

def sanitize_text(corpus):
	corpus = str(corpus)
	

if __name__ == "__main__":
	URL = "https://amp.theguardian.com//technology/2017/mar/30/lastpass-warns-users-to-exercise-caution-while-it-fixes-major-vulnerability"
	generate_word_cloud(URL, 'content__article-body from-content-api js-article__body')