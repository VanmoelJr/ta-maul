import os
import time
import psutil
import multiprocessing
from htmldom import htmldom

def ini_dom():
	
	dom = htmldom.HtmlDom('https://mmaul.tech/scrapeit').createDom()
	nama = dom.find("td[id=nama]")
	alamat = dom.find("td[id=alamat]")
	data = dom.find("td[id=data]")
	tgl = dom.find("td[id=tgl]")
	email = dom.find("td[id=email]")
	ssn = dom.find("td[id=ssn]")

	nm = [(n.text()) for n in nama]
	em = [(e.text()) for e in email]
	al = [(a.text()) for a in alamat]
	tg = [(t.text()) for t in tgl]
	sn = [(s.text()) for s in ssn]
	n = len(nm)
	e = len(em)
	t = len(tg)
	a = len(al)
	s = len(sn)

	print(nm,al,tg,em,sn)
	print("\nTotal Object Didapat :",n+e+t+a+s)

if __name__ == '__main__':
	start = time.time()
	memori1 = psutil.Process(os.getpid()).memory_info().rss
	up = psutil.net_io_counters().bytes_sent
	down = psutil.net_io_counters().bytes_recv
	cpu0 = psutil.cpu_percent()
	exe = multiprocessing.Process(target=ini_dom)
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