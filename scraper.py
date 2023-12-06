import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.century21.com/real-estate/atlanta-ga/LCGAATLANTA/")
c = r.content
soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class" : "property-card-primary-info"})
price = all[0].find("a", {"class" : "listing-price"}).text
#print(all)
#print(price.replace('\n', '').replace(' ',''))

for item in all:
    price = item.find("a", {"class" : "listing-price"}).text
    address = item.find("div" , {"class" : "property-address"}).text
    print(address.replace(' ','').replace('\n' , ''))
    city = item.find("div" , {"class" : "property-city"}).text
    print(city.replace('\n' , '').replace(' ', ''))
    try:
        beds = item.find("div" , {"class" : "property-beds"}).text
        print(beds.replace('\n', '').replace(' ', ''))
    except:
        print("No bed information available")
        pass
    try:
        baths = item.find("div" , {"class" : "property-baths"}).text
        print(baths.replace('\n', '').replace(' ', ''))
    except:
        print("No bath information available")
        pass
    print(price.replace('\n', '').replace(' ',''))
    print()
