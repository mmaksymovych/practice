import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = "https://news.ycombinator.com/"
response = requests.get(url)

if(response.status_code != 200):
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find and print all the article titles
titles = soup.select("span.titleline > a:first-of-type")  # class name may vary: also try '.titleline > a'

keyword = 'Apple'

for i, title in enumerate(titles[:10], 1):  # limit to top 10
        if(keyword.lower() in title.text.lower()):
            print(f"{i}. {title.text}")




