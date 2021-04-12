#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt install figlet")
os.system("clear")
os.system("figlet RAR-ZIP CRACK")
print("""

1) RAR Kırma
2) ZIP Kırma
3) Kırılan Şifreleri Göster


""")

secim = input("Seçim : ")

if(secim=="1"):	
	rar = input("RAR Dosyası : ")
	print("")
	os.system("sudo rar2john " + rar + " > hash.txt")
	os.system("sudo john hash.txt --pot=sifre.txt")


elif(secim=="2"):	
	zipdo = input("ZIP Dosyası : ")
	print("")
	os.system("sudo zip2john " + zipdo + " > hash.txt")
	os.system("sudo john hash.txt --pot=sifre.txt")

elif(secim=="3"):
	print("")
	os.system("sudo cat sifre.txt")


