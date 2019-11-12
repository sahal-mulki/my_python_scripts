import os
from cryptography.fernet import Fernet

try:
    FILE1 = open("OTP1.txt", "r")
except:
    FILE2 = open("OTP2.txt", "r")
cipher_text0 = input("Enter your phrase to be encrypted")
try:
    cipher_text = FILE1.encrypt("b" + cipher_text0)
    os.system("cd C:/UsersM.Sahal/Desktop/best projects")
    os.system("del [OTP1.txt]")
except:
    cipher_text = FILE2.encrypt("b" + cipher_text0)
    os.system("cd C:/Users/M.Sahal/Desktop/best projects")
    os.system("del [OTP2.txt]")
print(cipher_text + "is your encrypted text")
