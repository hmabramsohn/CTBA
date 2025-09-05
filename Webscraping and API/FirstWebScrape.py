import requests
from bs4 import BeautifulSoup

# GET request to Python events page
url = 'https://www.python.org/events/'
req = requests.get(url)

# Parsing HTML content into text
soup = BeautifulSoup(req.text, 'lxml')

# Find events list using html tag and class by searching the parsed HTML text
events = soup.find('ul', {'class':'list-recent-events'}).find_all('li')

# Use for loop to pull location for each event in events list
# Title, location, and date
for event in events:
    title = event.find('h3', {'class':'event-title'}).get_text(strip = True)
    location = event.find('span', {'class':'event-location'}).get_text(strip=True)
    date = event.find('time').get_text(strip=True)
    print(f"Title: {title}")
    print(f"Location: {location}")
    print(f"Date: {date}")