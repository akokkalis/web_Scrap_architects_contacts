from bs4 import BeautifulSoup

import requests


def contacts(url):

    mypage = requests.get(url)

    soup = BeautifulSoup(mypage.text, "html.parser")

    # print(doc.find_all(class_="contact-details"))
    name = soup.find(class_="company-slider-text")
    print(name.find("h1").text)
    name = name.find("h1").text

    contact_pe = soup.find_all(class_="addr-info")
    print(contact_pe[0].find_all("span")[1].text)

    contact_person = contact_pe[1].find_all("span")[0].text
    city = contact_pe[0].find_all("span")[1].text.strip()

    for a in soup.find_all(class_="contact-details"):
        try:
            email = soup.find("a", class_="mailto").text
            email = email.replace("[ at ]", "@").replace(" ", "")
        except:

            email = ""
        # print(email)
        # print(soup.find_all("span"))
        print(soup.find_all(class_="contact-details"))
        sib = soup.find_all(class_="contact-details")
        print()
        print()
        # print(soup.find_all("i", class_="fa fa-phone fa-fw"))
        ph = soup.find("i", class_="fa fa-phone fa-fw")
        ph1 = ph.find_next_sibling("span")
        print(ph1.text)
        phone = ""
        if ";" in ph1.text:
            # ph1.text.split(";")
            phone_list = ph1.text.split(";")
            phone = phone_list[0].strip().replace(" ", "")
            print(phone)
        else:
            phone = ph1.text.strip().replace(" ", "")
        return {
            "Business Name": name,
            "Contact Name": contact_person,
            "Email": email,
            "Phone": phone,
            "City": city,
        }
