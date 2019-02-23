from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://seth.blog/').text
#print(source)

soup = BeautifulSoup(source, 'lxml')

csv_file = open('seth_scrape.csv', 'wb')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])

for article in soup.find_all('div', class_='post'):
    headline = article.h2.a.text.encode('utf-8')
    print(headline)

    summary = article.div.p.text.encode('utf-8')
    print(summary)

    csv_writer.writerow([headline, summary])

csv_file.close()