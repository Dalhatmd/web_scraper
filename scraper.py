import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class" : "property-card-primary-info"})
