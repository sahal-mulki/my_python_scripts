import subprocess

import platform

target = input("Enter an IP or Host to ping:")

if platform == 'Windows' :

    host = subprocess.Popen(['ping', target], stdout = subprocess.PIPE).communicate()[0]

else :

    host = subprocess.Popen(['ping', target, "-c4",], stdout = subprocess.PIPE).communicate()[0]

print(host)

