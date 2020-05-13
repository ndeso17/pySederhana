import urllib.request
import os
import time
import sys

def sue(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(35. /100)
def lambatcetak(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. /100)
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)
def fastprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7. / 100)
def benar():
	os.system('python3 cerita.py')
def salah():
	pilihan = input('Jawaban => ')
	if pilihan == 'A' :
		slowprint('Salah hmmmm 🙅')
		salah()
	elif pilihan == 'a' :
		slowprint('Salah hmmmm 🙅')
		salah()
	elif pilihan == 'B' :
		slowprint('Dibaca yang benar...!!! 🙈')
		salah()
	elif pilihan == 'b' :
		slowprint('Dibaca yang benar...!!! 🙈')
		salah()
	elif pilihan == 'C' :
		lambatcetak('Yeahhhhh.....!!!')
		slowprint('Kenapa minta Dulangi sih? hmmmmmm ok deh aku ulang ceritanya')
		benar()
		salah()
	elif pilihan == 'c' :
		lambatcetak('Yeahhhhh.....!!!')
		slowprint('Kenapa minta Dulangi sih? hmmmmmm ok deh aku ulang ceritanya')
		benar()
		salah()
	elif pilihan == 'D' :
		fastprint('Yeah cerdik sekali. :v')
		fastprint('Selamat anda ternyata juga Jomblo kan? :v')
		fastprint('Mana mungkin ada CEUWE yang mau nungguin COWOnya main terus-terusan dengan PC,Laptop,atau HPnya.')
		fastprint('Kalau ada mending putusin ajh sumpah dah jangan dipertahankan buat aku saja. 😆')
		fastprint('Untuk membuat sebuah program ataupun sekedar main game. :v')
		time.sleep(5)
		lambatcetak('--------------------------------END--------------------------------')
		lambatcetak('By 🖖')
		exit()
	elif pilihan == 'd' :
		fastprint('Yeah cerdik sekali. :v')
		fastprint('Selamat anda ternyata juga Jomblo kan? :v')
		fastprint('Mana mungkin ada CEUWE yang mau nungguin COWOnya main terus-terusan dengan PC,Laptop,atau HPnya.')
		fastprint('Untuk membuat sebuah program ataupun sekedar main game. :v')
		fastprint('Kalau ada mending putusin ajh sumpah dah jangan dipertahankan buat aku saja. 😆')
		time.sleep(5)
		lambatcetak('--------------------------------END--------------------------------')
		lambatcetak('By 🖖')
		exit()
slowprint('''\033[92m............................Cah Kembar 3.......................
    Suatu ketika, hidup tiga anak kembar bernama Dulanga Dulango Dulangi. Mereka kakak adik yang kompak dan serasi. Pada suatu kesempatan mereka sudah memutuskan untuk menikah dengan masing-masing pasangannya yang telah dipilihkan oleh kedua orang tuannya. Dulanga menikah dengan pasangannya bernama Siti Marjanah, begitupun Dulango menikah dengan pasangannya juga bernama Siti Kurmaniah. Akan tetapi Dulangi belum bisa untuk menikahi pasangannya karena dia Jomblo. 😳 ''')
time.sleep(5)
print('										')
slowprint("------------------------------------------------------------------")
sue("\33[30;1mDari cerita diatas, reality siapakah yang Jomblo?")
lambatcetak("A. Dulanga")
lambatcetak("B. Dulango")
lambatcetak("C. Dulangi")
lambatcetak("D. Tidak ada yang jomblo")

pilihan = input('\33[31;1mJawaban => ')
if pilihan == 'A' :
	slowprint('\33[30;1mSalah hmmmm 🙅')
	salah()
elif pilihan == 'a' :
	slowprint('\33[30;1mSalah hmmmm 🙅')
	salah()
elif pilihan == 'B' :
	slowprint('\33[30;1mDibaca yang benar...!!! 🙈')
elif pilihan == 'b' :
	slowprint('\33[30;1mDibaca yang benar...!!! 🙈')
elif pilihan == 'C' :
	lambatcetak('\33[30;1mYeahhhhh.....!!!')
	slowprint('\33[30;1mKenapa minta Dulangi sih? hmmmmmm ok deh aku ulang ceritanya')
	os.system('python3 cerita.py')
elif pilihan == 'c' :
	lambatcetak('\33[30;1mYeahhhhh.....!!!')
	slowprint('\33[30;1mKenapa minta Dulangi sih? hmmmmmm ok deh aku ulang ceritanya')
	os.system('python3 cerita.py')
elif pilihan == 'D' :
	fastprint('\33[30;1mYeah cerdik sekali. :v')
	fastprint('\33[30;1mSelamat anda ternyata juga Jomblo kan? :v')
	fastprint('\33[30;1mMana mungkin ada CEUWE yang mau nungguin COWOnya main terus-terusan dengan PC,Laptop,atau HPnya.')
	fastprint('\33[30;1mKalau ada mending putusin ajh sumpah dah jangan dipertahankan buat aku saja. 😆')
	fastprint('\33[30;1mUntuk membuat sebuah program ataupun sekedar main game. :v')
	time.sleep(5)
	lambatcetak('--------------------------------END--------------------------------')
	lambatcetak('By 🖖')
	fastprint('Lah kok sewot? yang buat saya yh terserah donks saya mau ngetik kaya aph. :v')
	exit()
elif pilihan == 'd' :
	fastprint('\33[30;1mYeah cerdik sekali. :v')
	fastprint('Selamat anda ternyata juga Jomblo kan? :v')
	fastprint('Mana mungkin ada CEUWE yang mau nungguin COWOnya main terus-terusan dengan PC,Laptop,atau HPnya.')
	fastprint('Untuk membuat sebuah program ataupun sekedar main game. :v')
	fastprint('Kalau ada mending putusin ajh sumpah dah jangan dipertahankan buat aku saja. 😆')
	time.sleep(5)
	lambatcetak('--------------------------------END--------------------------------')
	lambatcetak('By 🖖')
	fastprint('Lah kok sewot? yang buat saya yh terserah donks saya mau ngetik kaya aph. :v')
	exit()
