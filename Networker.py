#For administration and maintainence purposes ONLY

import time
import subprocess
import os 
import webbrowser

print("Networker - Network Utility")

def networkly():

    print("1 - Remote Shutdown | 2 - Domain's UP | 3 - IPs on Network |")
    input0 = input(" 4 - Ip Information | 5 - Traceroute | 6 - Whois | 7 - Ping | 8 - Exit")
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
            p = subprocess.Popen(["ping", input1, "-n", "1"], stdout=subprocess.PIPE)
            ping0 = p.communicate()[0]
            ping = ping0.decode()
        
            if "not find" in ping:
                print(" ")
                print("Website is down! Website is down!")
                print("OR you just gave a wrong address")
                print("")
                print(ping)
                print(" ")
                input2 = input("ENTER to proceed")
                print("")
            else:
                print("Everything's Okay! YAY! 😊")
                print("")
                print(ping)
                print("")

    elif input0 == "3":
        i = subprocess.Popen(["arp", "-a"], stdout=subprocess.PIPE)
        ips0 = i.communicate()[0]
        ips_final = ips0.decode()
        print(ips_final)
        print("")

    elif input0 == "4":
        i = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
        ip0 = i.communicate()[0]
        ip_final = ip0.decode()
        print(ip_final)
        print("")

    elif input0 == "5":
        input3 = input("Address: ")
        i = subprocess.Popen(["tracert", input3], stdout=subprocess.PIPE)
        ip0 = i.communicate()[0]
        ip_final = ip0.decode()
        print(ip_final)
        print("")
                             
    elif input0 == "6":
        input4 = input("Address: ")
        webbrowser.open('https://who.is/whois/' + input4 + "")
        print("")
        
    elif input0 == "7":
        input3 = input("Address: ")
        i = subprocess.Popen(["ping", input3, "-n", "1"], stdout=subprocess.PIPE)
        ip0 = i.communicate()[0]
        ip_final = ip0.decode()
        print(ip_final)
        print("")
        
    elif input0 == "8":
        os._exit(0)

    else:
        print("")
        print("Invalid Option")
    
while True:
    networkly()
