import subprocess

import platform

print("By Sahal Mulki")
target = input("Enter an IP or Host to ping:")
print("Wait....")
host = subprocess.Popen(['ping', target], stdout = subprocess.PIPE).communicate()[0]

print(host)

