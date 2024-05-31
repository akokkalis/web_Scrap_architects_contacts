from bs4 import BeautifulSoup

import requests

from cy_architects_webscrap_one import contacts

import pandas as pd


def find_urls():
    links = []
    for i in range(1, 11):
        url = f"https://www.cyprusconstruction.com/cyprus-construction/page-{i}.html"
        mypage = requests.get(url)
        doc = BeautifulSoup(mypage.text, "html.parser")
        for a in doc.find_all(class_="wb-local-business"):
            print(a["href"])
            links.append(a["href"])
    return links


all_conpanies_urls = find_urls()
print(all_conpanies_urls)
print(len(all_conpanies_urls))

alist = []
for url in all_conpanies_urls:
    com_details = contacts(url)
    alist.append(com_details)

df = pd.DataFrame.from_dict(alist)
df.to_csv("cyprusconstrucions.csv", index=False)
