#For administration and maintainence purposes ONLY

import winsound
import time
import subprocess

print("Networker - Loading")

input0 = input("1 - remote_sdown | 2 - check_adress | 3 - check_ips")
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

elif input0 == "3":
    i = subprocess.Popen(["arp", "-a"], stdout=subprocess.PIPE)
    ips0 = i.communicate()[0]
    ips_final = ips0.decode()
    print(ips_final)
