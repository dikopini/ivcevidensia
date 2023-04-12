import requests
from bs4 import BeautifulSoup

url = 'https://ivcevidensia.co.uk/ems-choose-your-preferred-location'

res = requests.get(url)
print(res.text)
#soup = BeautifulSoup(res.text, 'html.parser')
#content = soup.find('div', 'jss166 jss167')
#item = soup.find_all('div', class_= ['jss244 jss245', 'jss244 jss260'])
