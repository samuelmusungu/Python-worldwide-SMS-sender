import telnyx
import string    
import random
from colorama import *
from colorama import Fore, Back, init
import os
import sys
import time
init(autoreset=True)
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
cy = Fore.CYAN
bwh = Back.WHITE
byl = Back.YELLOW
bred = Back.RED
bgr = Back.GREEN

os.system('title Telnyx Bulk SMS Sender ')
os.system('cls')
clear = '\x1b[0m'
colors = [36, 32, 34, 35, 31, 37]
x = '''

                       
  ______ _____   ______
 /  ___//     \ /  ___/
 \___ \|  Y Y  \\___ \ 
/____  >__|_|  /____  >
     \/      \/     \/ 

             
                
                '''
for N, line in enumerate(x.split('\n')):
    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
    time.sleep(0.05)
lt = []
with open("senderid.txt" ,"r") as file_name:
    print('=======================================================')
    print(f'{bgr}{wh}---> Reading your numbers')
    time.sleep(2)
    for  n in file_name.readlines():
        lt.append(n.replace("\n","").split(","))

with open("Leads.txt","r") as f:
    print(f'{bgr}{wh}---> Reading your leads')
    time.sleep(2)
    tsg=f.readlines()
with open("message.txt","r",) as f:
    print(f'{bgr}{wh}---> Reading your message')
    time.sleep(2)
    message=f.read()
def gen():
        S = 10    

        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        return ran

def send(id,num,msg):
   
   
    telnyx.api_key = id[0]

    your_telnyx_number = id[1]
    
    telnyx.Message.create(
    from_=your_telnyx_number,
    to=num,
    text=msg,
        )
     
t=0

for s in tsg:
   
    text=message
    try:
        if t==len(lt):
            t=0
        
        send(lt[t],s,text)
        t += 1
        print(f"{bwh}{bred}Message sent successfully to {s} ")
    except:
        print(f"{bwh}{bred}Message not sent successfully to {s}")
           
       
        



input("{ble}{cy}Press enter to exit")
