import csv
import re
import urllib.request
from bs4 import BeautifulSoup
from bible import books, ignore_words, class_name
import os

def preprocess_text(text):
    words = re.findall(r'\b\w+\b', text)
    filtered_words = [word.lower() for word in words if word.lower() not in map(str.lower, ignore_words)]
    return ' '.join(filtered_words)

def extract_content(url, class_name):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find('div', class_=class_name)
    text_result = element.get_text(separator=' ') if element else ''

    return preprocess_text(text_result)

base_url_esv = 'https://www.bible.com/bible/59/'
ill_part_esv = '.ESV'
urls_esv = [base_url_esv + f'{book}.{i}{ill_part_esv}' for book, chapters in books.items() for i in range(1, chapters + 1)]

base_url_ill15 = 'https://www.bible.com/bible/1097/'
ill_part_ill15 = '.ILL15'
urls_ill15 = [base_url_ill15 + f'{book}.{i}{ill_part_ill15}' for book, chapters in books.items() for i in range(1, chapters + 1)]

esv_words = []
ill15_words = []

for url in urls_esv:
    esv_words.append(extract_content(url, class_name))
    print(url)

for url in urls_ill15:
    ill15_words.append(extract_content(url, class_name))
    print(url)

csv_filename = os.path.join('..', 'lib', 'translations.csv')  # Path to lib folder in the parent directory
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ESV Words', 'ILL15 Words'])

    for esv_word, ill15_word in zip(esv_words, ill15_words):
        csv_writer.writerow([esv_word, ill15_word])

print("CSV file written:", csv_filename)
