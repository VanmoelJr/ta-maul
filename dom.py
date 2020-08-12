import os
import time
import psutil
import requests
from htmldom import htmldom

# Menghitung Waktu Proses
start = time.time()
# Menghitung Penggunaan Memori Start
memori1 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Upstream dan Downstream
up = psutil.net_io_counters().bytes_sent
down = psutil.net_io_counters().bytes_recv
#Menghitung Penggunaan CPU Dalam Persen
cpu0 = psutil.cpu_percent()

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

# End Time
end = time.time()
# Menghitung Penggunaan Memori End
memori2 = psutil.Process(os.getpid()).memory_info().rss
# Menghitung Bandwith Usage
up0 = psutil.net_io_counters().bytes_sent
down0 = psutil.net_io_counters().bytes_recv
# Hasil Persentase CPU
cpu = psutil.cpu_percent()

print(nm,al,tg,em,sn)
#print("\nTotal Object Didapat :",n+e+t+a+s)
# Hasil Penggunaan Memori
print("\nPenggunaan memory :",memori2-memori1,"bytes")
# Hasil Waktu Proses
print("Waktu proses :",end-start,"second")
# Hasil Bandwidth Upstream & Downstream
print("Penggunaan Bandwidth : Upstream =",up0-up,"Downstream = ",down0-down)
# Hasil Penggunaan CPU
print("CPU yang digunakan :",cpu-cpu0,"%")