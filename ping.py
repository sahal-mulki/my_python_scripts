import subprocess

import platform

__author__ = "Sahal Mulki"

print("Made by Sahal Mulki")
target = input("Enter an IP or Host to ping:")
print("Wait....")
host = subprocess.Popen(['ping', target], stdout = subprocess.PIPE).communicate()[0]

print(host)

