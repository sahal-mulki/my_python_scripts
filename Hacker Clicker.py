import pyautogui
import time
__author__ = "Sahal Mulki"

print("Made by Sahal Mulki")
print("     H     ")
print("     A     ")
print("     C     ")
print("     K     ")
print("     E     ")
print("     R     ")
print("           ")
print("     C     ")
print("     L     ")
print("     I     ")
print("     C     ")
print("     K     ")
print("     E     ")
print("     R     ")

print("(Y)es or (N)o")
inputabc = input("Should failsafe be on (mouse in top left corner will stop the program)")

if inputabc == "Y":
    pyautogui.FAILSAFE = True
elif inputabc == "N":
    pyautogui.FAILSAFE = False
    
input0 = input("Would you Like to hack (C)ookie Clicker or (D)oge Clicker")
 

if input0 == "C":

    input1 = input("Would you Like to (I)nfinity Tap or Tap the cookie a (S)pecified amount of times")
    
    if input1 == "I": 
        input2 = input("Place your cursor on the cookie and press ENTER")
        a = 1
        i = 0
        while a == 1:
            pyautogui.click()
            time.sleep(0.005)
            i += 1
            print(i)
    elif input1 == "S" :
        input3 = int(input("Enter number of times cookie will be clicked"))
        input4 = input("Place your cursor on the cookie and press ENTER")
        while input3 != 0:
            pyautogui.click()
            input3 -= 1
            time.sleep(0.0005)
            print(input3)
        if input3 == 0:
            print("DONE!")
            time.sleep(10)

elif input0 == "D":

    input6 = input("How many cycles do you want to execute?")
    input5 = input("Place your cursor on the ore and press ENTER")
    b = 1
    i = 0
    for x in range(int(input6)):
        for x in range(100):
            pyautogui.click()
            time.sleep(0.005)
            i += 1
            print(i)
        print("Collect your coins")
        time.sleep(2)
    
    
