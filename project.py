from bs4 import BeautifulSoup
import requests
import time, csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)

temp_list= []
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find('table')
tr = table.find_all('tr')
for t_r in tr:
    td = t_r.find_all("td")
    row = [e.text.strip() for e in td]
    temp_list.append(row)
headers = ["vmag", "name", "bayer_designation", "distance", "class", "mass", "radius", "kuminosity"]
with open("scrapper_5.csv", "w", encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(temp_list)
