from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()

scrape_site_url = os.getenv("SCRAPE_SITE")

html_text = requests.get(scrape_site_url).text
soup = BeautifulSoup(html_text, "lxml")
job = soup.find("header", class_="JobItem__header JobItem__header").text.replace(" ", "")
location = soup.find("span", class_="text-truncate").text.replace(" ", "")
print(job)
print(location)