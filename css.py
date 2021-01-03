import os
import time
import psutil
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.codelatte.org/maul/'
all_urls = list()

def rand_url():
    for i in range(5):
        all_urls.append(base_url + str(i))

def ini_css(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    sampel = soup.find('table', {'id':'example'})
    tbody = sampel.find('tbody')

    for tr in tbody.find_all('tr'):
        nomor = tr.find_all('td')[0].text.strip()
        nama = tr.find_all('td')[1].text.strip()
        alamat = tr.find_all('td')[2].text.strip()
        tgl = tr.find_all('td')[3].text.strip()
        email = tr.find_all('td')[4].text.strip()
        ssn = tr.find_all('td')[5].text.strip()
        print('|',nomor,'|',nama,'|',alamat,'|',tgl,'|',email,'|',ssn,'|')

rand_url()
# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
cpu0 = psutil.cpu_percent()

for url in all_urls:
    ini_css(url)

# End Time
end = time.time()
# Menghitung Penggunaan Memori End
memori2 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Usage
up0 = psutil.net_io_counters().bytes_sent
down0 = psutil.net_io_counters().bytes_recv
# Hasil Persentase CPU
cpu = psutil.cpu_percent()

# Hasil Penggunaan Memori
print("\nPenggunaan memory : {} bytes".format(memori2-memori1))
# Hasil Waktu Proses
print("Waktu proses : {} second".format(end-start))
# Hasil Bandwidth Upstream & Downstream
print("Penggunaan Bandwidth : Upstream = {} Downstream = {}".format(up0-up,down0-down))
# Hasil Penggunaan CPU
print("CPU yang digunakan : {} %".format(cpu))