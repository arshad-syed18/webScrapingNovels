import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# Set the base URL
base_url = 'https://novelfull.com/'

# Set the URL of the first chapter
url = urljoin(base_url, 'hidden-marriage/chapter-1-7-months-pregnant.html')

# Initialize a list to store the chapter dictionaries
chapters = []

# Loop to scrape all chapters
while True:
    # Send an HTTP request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the story text element and get its contents
    story_text = soup.find('div', {'id': 'chapter-content'})
    chapter_content = '\n'.join([p.text for p in story_text.find_all('p')])

    # Add the chapter dictionary to the list
    chapter_number = url.split('/')[-1].split('.')[0].split('-')[-1]
    chapter_dict = {'number': chapter_number, 'content': chapter_content}
    chapters.append(chapter_dict)

    # Find the "Next Chapter" button element and extract the URL of the next chapter
    next_chapter_button = soup.find('a', {'id': 'next_chap'})

    # if the next chapter button is none then the code will end
    if next_chapter_button is not None:
        next_chapter_url = next_chapter_button['href']
        url = urljoin(base_url, next_chapter_url)
    else:
        print("\n\nEnd")
        break # End the loop if there are no more chapters

# Save the chapters list to a JSON file
with open('C:/Users/arsha/OneDrive/Desktop/hidden-marriage.json', 'w') as f:
    json.dump(chapters, f)
