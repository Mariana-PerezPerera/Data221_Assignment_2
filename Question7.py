#import the requests and beautifulsoup packages:
import requests
from bs4 import BeautifulSoup

#assign the url of the webpage:
url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent" : "Mozilla/5.0"
}

#now we have to request to the webpage
response = requests.get(url, headers=headers)
#we have to make sure to catch the bad responses early:
response.raise_for_status()

#parsing the html with using beautiful soup:
parsed_html = BeautifulSoup(response.text, "html.parser")

#now we have to extract and print out the page title:
#for the first page title:
webpage_title = parsed_html.title.text.strip()
print("Webpage title:")
print(webpage_title)

#now we will work with the first paragraph from the main content:
content_div = parsed_html.find("div", id= "mw-content-text")

#make sure the main content div exists with an if statement:
if content_div:
    paragraphs = content_div.findAll("p")

    for p in paragraphs:
        text = p.get_text(strip=True)
        #making sure the rule of 50 characters is upheld:
        if len(text) >= 50:
            print("\nFirst paragraph (50+ characters):")
            print(text)
            break
else:
    print("Main content div is not found.")


