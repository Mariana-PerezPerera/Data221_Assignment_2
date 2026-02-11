#starting by importing requests as well as beautiful soup:
import requests
from bs4 import BeautifulSoup

#now we need to assign the url of the webpage:
url = "https://en.wikipedia.org/wiki/Data_science"

#now we are going to use the requests package and send requests with headers:
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()

#now we have to parse the HTML using beautiful soup:
parsed_html = BeautifulSoup(response.text, "html.parser")

#now we have to find the main content area:
content_div = parsed_html.find("div", id="mw-content-text")

#we have to make sure to exclude certain words/headings:
excluded_words = ["References", "External links", "See also", "Notes"]

#creating an empty list for all the valid section headings that will be extracted:
headings = []

#check is the main content exists:
if content_div:
    #now we have to find all the h2 headings inside main content
    h2_tags = content_div.find_all("h2")

#looping through each of the headings:
    for h2 in h2_tags:
        #extract all the heading text:
        heading_text = h2.get_text(strip=True)
        #now we have to remove the [edit] text
        heading_text = heading_text.replace("[edit]", "").strip()
        #skipping the excluded headings:
        if any(word in heading_text for word in excluded_words):
            continue
        headings.append(heading_text)

    #lastly, we have to save these headings to a file:
    with open("headings.txt", "w",) as file:
    #create and open the file (headings.txt) in write mode:
        for heading in headings:
            file.write(heading + "\n")
