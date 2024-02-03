import csv
import re
import urllib.request
from bs4 import BeautifulSoup

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

    return text_result, filtered_words

# Books of the Bible with their respective chapter counts
books = {
    'GEN': 50, 'EXO': 40, 'LEV': 27, 'NUM': 36, 'DEU': 34,
    'JOS': 24, 'JDG': 21, 'RUT': 4, '1SA': 31, '2SA': 24,
    '1KI': 22, '2KI': 25, '1CH': 29, '2CH': 36, 'EZR': 10,
    'NEH': 13, 'EST': 10, 'JOB': 42, 'PSA': 150, 'PRO': 31,
    'ECC': 12, 'SNG': 8, 'ISA': 66, 'JER': 52, 'LAM': 5,
    'EZK': 48, 'DAN': 12, 'HOS': 14, 'JOL': 3, 'AMO': 9,
    'OBA': 1, 'JON': 4, 'MIC': 7, 'NAM': 3, 'HAB': 3,
    'ZEP': 3, 'HAG': 2, 'ZEC': 14, 'MAL': 4,
    'MAT': 28, 'MRK': 16, 'LUK': 24, 'JHN': 21, 'ACT': 28,
    'ROM': 16, '1CO': 16, '2CO': 13, 'GAL': 6, 'EPH': 6,
    'PHP': 4, 'COL': 4, '1TH': 5, '2TH': 3, '1TI': 6,
    '2TI': 4, 'TIT': 3, 'PHM': 1, 'HEB': 13, 'JAS': 5,
    '1PE': 5, '2PE': 3, '1JN': 5, '2JN': 1, '3JN': 1,
    'JUD': 1, 'REV': 22
}

# Common class_name and ignore_words
class_name = 'ChapterContent_reader__Dt27r'
ignore_words = ['div', 'style', 'p', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'h1', 'font', 'size', '18px', 'font', 'family', 'Inter', 'data', 'iso6393', 'bem', 'data', 'vid', '1097', 'class', 'version', 'vid1097', 'iso6393bem', 'class', 'ChapterContent_book__VkdB2', 'data', 'usfm', 'GEN', 'class', 'ChapterContent_chapter__uvbXo', 'class', 'ChapterContent_label__R2PLt']

# Generating URLs
base_url = 'https://www.bible.com/bible/1097/'
ill_part = '.ILL15'
urls = [base_url + f'{book}.{i}{ill_part}' for book, chapters in books.items() for i in range(1, chapters + 1)]

# Writing words to CSV file
csv_filename = 'extracted_words.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word'])

    for url in urls:
        text_result, words_result = extract_content(url, class_name, ignore_words)
        csv_writer.writerows([[word] for word in words_result])

        print("Text extracted from class for", url, ":")
        print(text_result)

print("\nFiltered words written to CSV file:", csv_filename)
