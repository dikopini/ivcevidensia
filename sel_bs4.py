import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# Fungsi untuk mendownload logo klinik
def download_logo(url, name):
    try:
        urllib.request.urlretrieve(url, name)
    except:
        pass

# URL website
url = 'https://ivcevidensia.co.uk/ems-choose-your-preferred-location'

# Melakukan request ke website
response = requests.get(url)

# Mengekstraksi data dari response menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari elemen HTML yang berisi data klinik
clinics = soup.find_all('div', {'class': 'col-md-4'})

# Inisialisasi counter
counter = 0

# Membuat folder untuk menyimpan logo
if not os.path.exists('logos'):
    os.makedirs('logos')

# Looping untuk mengambil data dari setiap klinik
for clinic in clinics:
    # Mengambil nama klinik
    name = clinic.find('h4', {'class': 'media-heading'}).text.strip()
    # Mengambil alamat klinik
    address = clinic.find('p', {'class': 'address'}).text.strip()
    # Mengambil URL logo klinik
    logo_url = clinic.find('img', {'class': 'img-responsive'})['src']
    # Mengambil nama file logo
    logo_name = 'logos/' + name.replace(' ', '_').lower() + '.jpg'
    # Mendownload logo klinik
    download_logo(logo_url, logo_name)
    # Mencetak data klinik
    print('Nama klinik:', name)
    print('Alamat:', address)
    print('URL logo:', logo_url)
    print('Nama file logo:', logo_name)
    print('---')
    # Mengecek apakah sudah terambil 400 data
    counter += 1
    if counter == 400:
        break
