import requests
from datetime import date

class gtrend:
	def __init__(self):
		self.tanggal = date.today()
		self.api = "https://trends.google.co.id/trends/api/dailytrends?hl=in&tz=-420&geo=ID&ns=15"
	def daily(self):
		print(f"Menampilkan Hasil Google Trend Pada {self.tanggal}")
		date = str(self.tanggal).replace("-", "")
		req = requests.get(self.api+"&ed="+date, allow_redirects=False)
		response = str(req.text).replace(")]}',", "")
		with open("result"+date+".txt", "w+", encoding='utf-8') as hasil:
			hasil.write(str(response))

	# def kemarin(self):
		

	# def mingguterakhir(self):
		

# Program utama
def main():
	print("Google Trends Grabber")
	print("Creator : Shizuo Code")
	print("Tools ini bermanfaat untuk mengambil judul artikel yang trending di Indonesia")
	print("Fitur : ")
	print("1. Hari ini")
	print("2. Sehari sebelumnya")
	print("3. Seminggu terakhir")
	pilih = int(input("Pilih menu : "))
	if pilih>=1 and pilih<=3:
		googletrend = gtrend()
		if pilih==1:
			googletrend.daily()
		elif pilih==2:
			googletrend.lastday()
		elif pilih==3:
			googletrend.weeks()
	else:
		print("Masukan Pilihan 1 sd. 3 saja !")
		main()

main()