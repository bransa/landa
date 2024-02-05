import csv
import re
import urllib.request
from bs4 import BeautifulSoup
from bible import books, ignore_words, class_name

def extract_content(url, class_name, ignore_words=None):
    if ignore_words is None:
        ignore_words = []

    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find('div', class_=class_name)
    text_result = element.get_text(separator=' ') if element else ''

    words = re.findall(r'\b\w+\b', text_result)
    filtered_words = [word.lower() for word in words if word.lower() not in map(str.lower, ignore_words)]

    unique_words_set = set()
    filtered_words = []

    for word in words:
        lowercase_word = word.lower()
        if lowercase_word not in map(str.lower, ignore_words) and lowercase_word not in unique_words_set:
            unique_words_set.add(lowercase_word)
            filtered_words.append(lowercase_word)

    merged_text_result = ' '.join(filtered_words)

    return merged_text_result, filtered_words

base_url_esv = 'https://www.bible.com/bible/59/'
ill_part_esv = '.ESV'
urls_esv = [base_url_esv + f'{book}.{i}{ill_part_esv}' for book, chapters in books.items() for i in range(1, chapters + 1)]

base_url_ill15 = 'https://www.bible.com/bible/1097/'
ill_part_ill15 = '.ILL15'
urls_ill15 = [base_url_ill15 + f'{book}.{i}{ill_part_ill15}' for book, chapters in books.items() for i in range(1, chapters + 1)]

csv_filename = 'translations.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['key', 'value', 'ill15'])

    for url in urls_esv:
        text_result, words_result = extract_content(url, class_name, ignore_words)
        csv_writer.writerows([[word, text_result, ''] for word in words_result])

        print(url, ":")
        print(text_result)

    for url in urls_ill15:
        text_result, words_result = extract_content(url, class_name, ignore_words)
        csv_writer.writerows([[word, '', text_result] for word in words_result])

        print(url, ":")
        print(text_result)

print(csv_filename)
