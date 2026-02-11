#we have to import requests, beautiful soup and csv:
import requests
import csv
from bs4 import BeautifulSoup

#assign the webpage to url:
url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()

#parse the html:
parsed_html = BeautifulSoup(response.text, "html.parser")

#finding the main content:
content_div = parsed_html.find("div", id="mw-content-text")

#making an empty list for the table data from the webpage and the headers:
table_data = []
headers_row = []

if content_div:
    tables = content_div.find_all("table")

    for table in tables:
        rows = table.find_all("tr")

        #make sure that the table has at least 3 data rows (finding the first table that has at least 3 data rows)
        if len(rows) < 4:
            continue

        #now we can extract the headers (from the th):
        header_cells = rows[0].find_all("th")
        if header_cells:
            headers_row = [th.get_text(strip=True) for th in header_cells]
        #if not we have to auto generate the headers named col.
        else:
            first_data_cells = rows[1].find_all("td")
            headers_row = [f"col{index+1}" for index in range(len(first_data_cells))]

        #extracting all the data rows:
        for row in rows[1:]:
            cells = row.find_all(["td", "th"])
            row_data = [cell.get_text(strip=True) for cell in cells]

            #handle all the uneven rows the missing values with a while loop:
            while len(row_data) < len(headers):
                row_data.append("")

            table_data.append(row_data)

        break

#now we have to save everything into a csv:
with open("wiki_table.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers_row)
    writer.writerows(table_data)
