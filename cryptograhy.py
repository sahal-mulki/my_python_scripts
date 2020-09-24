from cryptography.fernet import Fernet
import time
import pyperclip

def make_unicode(input2):
    input2 = input2.decode('utf-8')
    return input2

key = Fernet.generate_key()
f = Fernet(key)


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
        print("Its pasted to your clipboard paste it somewhere")
        pyperclip.copy(key)
        inputnoi = input("Press Enter when you are done pasting")
    secure_secret = f.encrypt(secret)
    secure_secret = str(secure_secret, 'utf-8')

    print("Encrypting......")
    print("[O     ]")
    time.sleep(1)
    print("[OO    ]")
    time.sleep(0.25)
    print("[OOO   ]")
    time.sleep(0.25)
    print("[OOOO  ]")
    time.sleep(0.25)
    print("[OOOOO ]")
    time.sleep(0.25)
    print("[OOOOOO]")
    print("Encryption complete , here's the encrypted string : " + str(secure_secret))
    print("String copied to clipboard")
    pyperclip.copy(str(secure_secret))

if input1 == "D":
    secret1 = input("Copy your encrypted string to your clipboard and press Enter")
    secret = pyperclip.paste()
    key1 = input("Copy your key to your clipboard and press ENTER")
    key = pyperclip.paste()
    secret2 = bytes(secret, 'utf-8')
    f = Fernet(key)
    print("The decrypted string is :")
    final = f.decrypt(secret2)
    final2 = make_unicode(final)
    print(final2)
    print("String copied to clipboard")
    pyperclip.copy(final2)

input1000000 = input("")
