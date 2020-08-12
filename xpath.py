import os
import time
import psutil
import requests
from lxml import html

# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
cpu0 = psutil.cpu_percent()

# Proses parsing data - scraping
site = requests.get('https://mmaul.tech/scrapeit')
data = html.fromstring(site.content)
nama = data.xpath("//td[@id='nama']/text()")
alamat = data.xpath("//td[@id='alamat']/text()")
tgl = data.xpath("//td[@id='tgl']/text()")
email = data.xpath("//td[@id='email']/text()")
ssn = data.xpath("//td[@id='ssn']/text()")

# Menghitung Jumlah Object Didapat 
list_nama = len(nama)
list_almat = len(alamat)
list_tgl = len(tgl)
list_email = len(email)
list_ssn = len(ssn)

# End Time
end = time.time()
# Menghitung Penggunaan Memori End
memori2 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Usage
up0 = psutil.net_io_counters().bytes_sent
down0 = psutil.net_io_counters().bytes_recv
# Hasil Persentase CPU
cpu = psutil.cpu_percent()

# Hasil Scraping Data
print(nama,alamat,tgl,email,ssn)
"""
# Hasil Object Didapat
print("Object nama didapat :", list_nama)
print("Object alamat didapat :", list_almat)
print("Object tanggal didapat :", list_tgl)
print("Object email didapat :", list_email)
print("Object ssn didapat :", list_ssn)"""
print("\nTotal object didapat :", list_nama+list_almat+list_email+list_tgl+list_ssn)
# Hasil Penggunaan Memori
print("Penggunaan memory :",memori2-memori1,"bytes")
# Hasil Waktu Proses
print("Waktu proses :",end-start,"second")
# Hasil Bandwidth Upstream & Downstream
print("Penggunaan Bandwidth : Upstream =",up0-up,"Downstream = ",down0-down)
# Hasil Penggunaan CPU
print("CPU yang digunakan :",cpu-cpu0,"%")