from bs4 import BeautifulSoup

import requests


import pandas as pd

import re

final_dict_list = []

for district in range(1, 7):
    for page in range(1, 3):
        url = f"https://seapek.org.cy/members/?district={district}&page={page}"
        mypage = requests.get(url)
        soup = BeautifulSoup(mypage.text, "html.parser")

        print(soup)

        all_name = soup.find_all(class_="post-title")
        names_list = []
        for name in all_name:
            names_list.append(name.text)

        address = soup.find_all(class_="address")
        print(address)
        add_list = []
        for add in address:
            print("")
            print
            mylist = []
            for index, p_tag in enumerate(add.find_all("p")):
                mylist.append(p_tag.text)
            add_list.append(mylist)

        print(add_list)
        print(len(add_list))
        print(len(names_list))

        if len(names_list) == len(add_list):
            for index, add in enumerate(add_list):
                add.insert(0, names_list[index])

        print(add_list)

        phone_pattern = r"\d{2} \d{6}|\d{8}"
        for index, company in enumerate(add_list):
            new_dict = {}
            for num, item in enumerate(company):
                print(num)
                print(item)

                matches = re.findall(phone_pattern, item)
                print(matches)
                if num == 0:
                    new_dict["Company Name"] = item
                if num == 1:
                    whole_address = item.split(",")
                    print(whole_address)
                    city = whole_address[-1].strip()
                    address = "".join(whole_address[0:-1])
                    new_dict["City"] = city
                    new_dict["Address"] = address
                if matches:
                    print("Phone")
                    print(matches)
                    print(item)
                    new_dict["Phone"] = item

                if "@" in item:
                    new_dict["Email"] = item

                if "www" in item:
                    new_dict["website"] = item

            print(new_dict)
            final_dict_list.append(new_dict)

df = pd.DataFrame.from_dict(final_dict_list)
df.to_csv("seapek.csv", encoding="UTF-8", index=False)
