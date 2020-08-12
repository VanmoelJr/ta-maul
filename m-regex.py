import re
import os
import time
import psutil
import urllib.request
import multiprocessing

def ini_regex():
	response = urllib.request.urlopen('https://mmaul.tech/scrapeit').read()
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

if __name__ == '__main__':
	start = time.time()
	memori1 = psutil.Process(os.getpid()).memory_info().rss
	up = psutil.net_io_counters().bytes_sent
	down = psutil.net_io_counters().bytes_recv
	cpu0 = psutil.cpu_percent()
	exe = multiprocessing.Process(target=ini_regex)
	exe.start()

	end = time.time()
	memori2 = psutil.Process(os.getpid()).memory_info().rss
	up0 = psutil.net_io_counters().bytes_sent
	down0 = psutil.net_io_counters().bytes_recv
	cpu = psutil.cpu_percent()
	exe.join()

	print("\nPenggunaan memory :",memori2-memori1,"bytes")
	print("Waktu proses :",end-start,"second")
	print("Penggunaan Bandwidth : Upstream =",up0-up,"Downstream = ",down0-down)
	print("CPU yang digunakan :",cpu-cpu0,"%\n")