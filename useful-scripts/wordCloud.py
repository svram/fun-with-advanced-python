# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
	A word cloud is visual representation of the frequency of words in a corpus 
	with frequency of the word directly proportional to its font size in the representation

	Now the first step in creating the word cloud is to clean the corpus removing
	unnecessary punctuation. The next step is the hard part.

	Does the apostrophe count as punctuation? What if someone uses the word "How's" instead of "How is"
	What about the underscore and the "-"?
	Would you treat uppercase, capitalised and lowercase differently?
	How about personal nouns?
	What about a word which is context dependent? Like "Hello Jack" and "This is a jack hammer"

	Dependig upon the situation, you would make a decision on the tradeoffs.
	Here are the assumptions we are going with:
		- We will not treat -, _ and ' as punctuation
		- Uppercase words will be converted to lowercase and trated as the same (hello and HELLO will be trated as 2 'hello')
		- Capitalised words will be kept as-is until a lowercase word is found in which case the capitalised word
		  will be converted to lowercase (Jack will remain as such until its lowercase version is found)

	We will be using a dictionary to store our "word:frequency" relationship.

	INPUT: URL of page we want to create a word clud of
	OUTPUT: HTML file with word cloud
	
	© 2017 Vikram Bahl

'''

import bs4

def generate_word_cloud(URL):
	#we extract the text from the page using beautiful soup library.
	#check out the scraping.py file for an intro to beautiful soup

def create_word_cloud(corpus):
	pass

def sanitize_text(corpus):
	pass

if __name__ == "__main__":
	URL = "https://www.nytimes.com/2017/03/29/technology/samsung-after-combustible-galaxy-note-7-unveils-new-smartphone.html"
	generate_word_cloud(URL)