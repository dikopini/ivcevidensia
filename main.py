import requests
from bs4 import BeautifulSoup

url = 'https://ivcevidensia.co.uk/ems-choose-your-preferred-location'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())