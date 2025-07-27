# Web Scraping: Automate Data Collection
# Python can scrape information automatically.
# Author: Piseth CHUON

import requests
from bs4 import BeautifulSoup

<<<<<<< HEAD
<<<<<<< HEAD

# blog URL
=======
# Blog URL
>>>>>>> de748c7c51f2d023b576f588e98cb1dd9bb74fcd
=======
# blog URL

>>>>>>> ab96bbb0a896f1bcf7550d0ca7eca2598fd0ca1b
url = "https://realpython.com"

print(f"Fetching data from {url}...")

# Send a GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Request successful! Parsing HTML...")
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and print all <h2> elements
    titles = soup.find_all("h2")

    if titles:
        print("Found the following titles:")
        for title in titles:
            print(title.text)
    else:
        print("No <h2> elements found on this page.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")