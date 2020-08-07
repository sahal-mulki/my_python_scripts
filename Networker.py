#For administration and maintainence purposes ONLY

import winsound
import time
import subprocess
import os 

print("Networker - Network Utility")

def networkly():

    input0 = input("1 - Remote Shutdown | 2 - Domain's UP | 3 - IPs on Network | 4 - Ip Information | 5 - Exit")
    if input0 == "1":
    
        print("Ip Address of Person")
        input1000 = input("")

        print("Message")
        input2000 = input("")
    
        os.system("shutdown /m " + input1000 + " /r /c  " + input2000 + "")
        print("Task done")

    elif input0 == "2":
        input1 = input("Domain Name")
        while True:
            try:
                time.sleep(0.50)
                p = subprocess.Popen(["ping", input1], stdout=subprocess.PIPE)
                ping0 = p.communicate()[0]
                ping = ping0.decode()
        
                if "not find" in ping:
                    print(" ")
                    print("Website is down! Website is down!")
                    print("OR you just gave a wrong address")
                    winsound.Beep(1000, 250)
                    winsound.Beep(1000, 250)
                    winsound.Beep(1000, 250)
                    winsound.Beep(1000, 250)
                    print(" ")
                    input2 = input("ENTER to proceed")
                else:
                    print("Everything's Okay! YAY! 😊")
            except KeyboardInterrupt:
                print("Exiting....")
                os._exit()
    elif input0 == "3":
        i = subprocess.Popen(["arp", "-a"], stdout=subprocess.PIPE)
        ips0 = i.communicate()[0]
        ips_final = ips0.decode()
        print(ips_final)

    elif input0 == "4":
        i = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
        ip0 = i.communicate()[0]
        ip_final = ip0.decode()
        print(ip_final)
    
    elif input0 == "5":
        os._exit()

while True:
    networkly()
