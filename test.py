import requests
import lxml.html

html = requests.get('https://mmaul.tech/scrapeit')
doc = lxml.html.fromstring(html.content)

nama = doc.xpath("//td[@id='nama']/text()")
alamat = doc.xpath("//td[@id='alamat']/text()")
tgl = doc.xpath("//td[@id='tgl']/text()")
email = doc.xpath("//td[@id='email']/text()")
ssn = doc.xpath("//td[@id='ssn']/text()")

print(nama)