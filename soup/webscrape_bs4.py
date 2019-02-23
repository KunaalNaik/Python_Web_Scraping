# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests

with open('samplesite.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    

#match = soup.title.text
#print(match)

#match = soup.div
#print(match)

#Gives the same output as above
#match = soup.find('div')
#print(match)

#However, we could not use class_ to indentify which different div's 
#match = soup.find('div', class_='footer')
#print(match)

#Lets extract the Articles
#article = soup.find('div', class_='article')
#print(article)

#headline = article.h2.a.text
#print(headline) 

#summary = article.p.text
#print(summary)    

#Now do it for all the articles
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)     
    summary = article.p.text
    print(summary)    
    

