import os
import time
import psutil
import requests
import multiprocessing
from bs4 import BeautifulSoup

def ini_css():
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
		print(' | ',nomor,' | ',nama,' | ',alamat,' | ',tgl,' | ',email,' | ',ssn,' | \n')

if __name__ == '__main__':
	start = time.time()
	memori1 = psutil.Process(os.getpid()).memory_info().rss
	up = psutil.net_io_counters().bytes_sent
	down = psutil.net_io_counters().bytes_recv
	cpu0 = psutil.cpu_percent()
	exe = multiprocessing.Process(target=ini_css)
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