import os
import time
import psutil
import requests
from bs4 import BeautifulSoup

# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
cpu0 = psutil.cpu_percent()

data = requests.get('https://mmaul.tech/scrapeit')
soup = BeautifulSoup(data.text, 'html.parser')
sampel = soup.find('table', { 'id': 'example'})
tbody = sampel.find('tbody')

for tr in tbody.find_all('tr'):
	nomor = tr.find_all('td')[0].text.strip()
	nama = tr.find_all('td')[1].text.strip()
	alamat = tr.find_all('td')[2].text.strip()
	tgl = tr.find_all('td')[3].text.strip()
	email = tr.find_all('td')[4].text.strip()
	ssn = tr.find_all('td')[5].text.strip()
	print(' | ',nomor,' | ',nama,' | ',alamat,' | ',tgl,' | ',email,' | ',ssn,' | ')

# End Time
end = time.time()
# Menghitung Penggunaan Memori End
memori2 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Usage
up0 = psutil.net_io_counters().bytes_sent
down0 = psutil.net_io_counters().bytes_recv
# Hasil Persentase CPU
cpu = psutil.cpu_percent()

#print("\nTotal Object Didapat :",n+e+t+a+s)
# Hasil Penggunaan Memori
print("\nPenggunaan memory :",memori2-memori1,"bytes")
# Hasil Waktu Proses
print("Waktu proses :",end-start,"second")
# Hasil Bandwidth Upstream & Downstream
print("Penggunaan Bandwidth : Upstream =",up0-up,"Downstream = ",down0-down)
# Hasil Penggunaan CPU
print("CPU yang digunakan :",cpu-cpu0,"%")