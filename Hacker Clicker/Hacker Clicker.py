import pyautogui
import time
import os
import pyscreeze

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
    
input0 = input("Would you Like to hack (C)ookie Clicker or (D)oge Clicker")
 

if input0 == "C":

    input1 = input("Would you Like to (I)nfinity Tap or Tap the cookie a (S)pecified amount of times")
    
    if input1 == "I": 


        screen = pyscreeze.screenshot()
        cookie = pyscreeze.locateOnScreen('cookie.png')
        cookiex, cookiey = pyscreeze.center(cookie)

        pyautogui.moveTo(cookiex, cookiey)

        i = 0
        while True:
            pyautogui.click()
            time.sleep(0.0005)
            i += 1
            print(i)
    elif input1 == "S" :
        input3 = int(input("Enter number of times cookie will be clicked"))
        
        screen = pyscreeze.screenshot()
        cookie = pyscreeze.locateOnScreen('cookie.png')
        cookiex, cookiey = pyscreeze.center(cookie)

        pyautogui.moveTo(cookiex, cookiey)
        
        while input3 != 0:
            try:
                pyautogui.click()
                input3 -= 1
                time.sleep(0.0005)
                print(input3)
            except:
                print("Error")
                
        if input3 == 0:
            print("DONE!")
            time.sleep(10)

elif input0 == "D":

    input6 = input("How many cycles do you want to execute?")
    input7 = input("Put your cursor on rock")
    
    i = 0
    for x in range(int(input6)):
        for x in range(100):
            
            pyautogui.click()
            time.sleep(0.0005)
            i += 1
            print(i)
        print("Collect your coins")
        time.sleep(3)
    
    
