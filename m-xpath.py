import os
import time
import psutil
import requests
import multiprocessing
from lxml import html

def ini_xpath():
	response = requests.get('https://mmaul.tech/scrapeit')
	data = html.fromstring(response.content)
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

	end = time.time()
	memori2 = psutil.Process(os.getpid()).memory_info().rss
	up0 = psutil.net_io_counters().bytes_sent
	down0 = psutil.net_io_counters().bytes_recv
	cpu = psutil.cpu_percent()
	
	print(nama,alamat,tgl,email,ssn,"\n")
	print("Total object didapat :", list_nama+list_almat+list_email+list_tgl+list_ssn)

if __name__ == '__main__':
	start = time.time()
	memori1 = psutil.Process(os.getpid()).memory_info().rss
	up = psutil.net_io_counters().bytes_sent
	down = psutil.net_io_counters().bytes_recv
	cpu0 = psutil.cpu_percent()
	exe = multiprocessing.Process(target=ini_xpath)
	exe.start()

	end = time.time()
	memori2 = psutil.Process(os.getpid()).memory_info().rss
	up0 = psutil.net_io_counters().bytes_sent
	down0 = psutil.net_io_counters().bytes_recv
	cpu = psutil.cpu_percent()
	exe.join()

	print("Penggunaan memory :",memori2-memori1,"bytes")
	print("Waktu proses :",end-start,"second")
	print("Penggunaan Bandwidth : Upstream =",up0-up,"Downstream = ",down0-down)
	print("CPU yang digunakan :",cpu-cpu0,"%")