import os
import time
import psutil
import requests
from lxml import html

base_url = 'https://www.codelatte.org/maul/'
all_urls = list()

def rand_url():
	for i in range(5):
		all_urls.append(base_url + str(i))

def ini_xpath(url):
	site = requests.get(url)
	data = html.fromstring(site.content)
	nama = data.xpath("//td[@id='nama']/text()")
	alamat = data.xpath("//td[@id='alamat']/text()")
	tgl = data.xpath("//td[@id='tgl']/text()")
	email = data.xpath("//td[@id='email']/text()")
	ssn = data.xpath("//td[@id='ssn']/text()")

	list_nama = len(nama)
	list_almat = len(alamat)
	list_tgl = len(tgl)
	list_email = len(email)
	list_ssn = len(ssn)

	print(nama,tgl,email,alamat,ssn)
	print("\nTotal Objek didapat : {}".format(list_nama+list_almat+list_email+list_tgl+list_ssn))

rand_url()
# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
#cpu0 = psutil.cpu_percent()

for url in all_urls:
    ini_xpath(url)

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