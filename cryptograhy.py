# USE AT YOUR OWN RISK
# THIS IS NOT FULLY SECURE ENCRYPTION
# IF ITS A REALLY IMPORTANT THING USE 
# A MORE SECURE ENCRYPTION ALGORITHM

from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)

prin("By Sahal Mulki")
input1 = input("(E)ncrypt or (D)ecrypt")


if input1 == "E":
    secret = input("What do you need to encrypt?")
    secret = bytes(secret, 'utf-8')
    input2 = input("Enter your key if any")
    if input2 != "":
        fernet_string = input2
        f = Fernet(fernet_string)
    if input2 == "":
        key = key.decode('utf-8')
        print("Here's your key : " + key)
    secure_secret = f.encrypt(secret)
    secure_secret = str(secure_secret, 'utf-8')
    print("Encryption complete , here's the encrypted string : " + str(secure_secret))

    
