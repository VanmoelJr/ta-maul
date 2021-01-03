import re
import os
import time
import psutil
import urllib.request
from multiprocessing import Pool

base_url = 'https://www.codelatte.org/maul/'
all_urls = list()

def rand_url():
	for i in range(5):
		all_urls.append(base_url + str(i))

def ini_regex(url):
	response = urllib.request.urlopen(url).read()
	text = response.decode()
	cari_nama = re.compile("<td id='nama'>(.*)</td>")
	cari_alamat = re.compile("<td id='alamat'>(.*)</td>")
	cari_tgl = re.compile("<td id='tgl'>(.*)</td>")
	cari_email = re.compile("<td id='email'>(.*)</td>")
	cari_ssn = re.compile("<td id='ssn'>(.*)</td>")

	nama = re.findall(cari_nama,text)
	alamat = re.findall(cari_alamat,text)
	email = re.findall(cari_email,text)
	tgl = re.findall(cari_tgl,text)
	ssn = re.findall(cari_ssn,text)
	
	batch = []
	batch[:] = range(1)
	for i in batch:
		print(nama,tgl,email,alamat,ssn)
	print("\nTotal Objek didapat : {}".format(len(nama)+len(email)+len(tgl)+len(alamat)+len(ssn)))

rand_url()

p = Pool(10)
# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
#cpu0 = psutil.cpu_percent()
p.map(ini_regex, all_urls)
p.terminate()
p.join()

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