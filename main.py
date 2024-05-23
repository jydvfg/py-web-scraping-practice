from bs4 import BeautifulSoup
import requests
import os
import time
from dotenv import load_dotenv
load_dotenv()

scrape_site_url = os.getenv("SCRAPE_SITE")
url_head = os.getenv("URL_HEAD")
print("Please enter your seniority")
seniority = input(">")
print(f"Displaying only {seniority} level jobs")

def find_jobs():
    html_text = requests.get(scrape_site_url).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("div", class_="JobItemWrapper")
    for index, job in enumerate(jobs):
        title = job.find("header", class_="JobItem__header JobItem__header" ).text.replace(" ", "")
        location = job.find("span", class_="text-truncate").text.replace(" ", "")
        description = job.find("div", class_="JobItem__content text-muted").text
        link = job.a["href"]
        if seniority in description: 
            with open(f"posts/{index}.txt", "w", encoding="utf-8") as f:
                
                f.write(f"Job title: {title.strip()} \n")
                f.write(f"Location: {location.strip()} \n")
                f.write(f"Description: {description.strip()} \n")
                f.write(f"More Info: {url_head}{link} \n")
            print(f"File saved: {index}")
   

if __name__ == "__main__":
    while True:
        find_jobs()
        print("Refreshing in 24h")
        time.sleep(86400)