from winput import *
import time



print("     C     ")
print("     O     ")
print("     O     ")
print("     K     ")
print("     I     ")
print("     E     ")
print("           ")
print("     C     ")
print("     L     ")
print("     I     ")
print("     C     ")
print("     K     ")
print("     E     ")
print("     R     ")


input1 = input("Would you Like to (I)nfinity Tap or Tap the cookie a (S)pecified amount of times")

if input1 == "I": 
    input2 = input("Place your cursor on the cookie and press ENTER")
    x = 1
    i = 0
    while x == 1:
        press_mouse_button(LEFT_MOUSE_BUTTON)
        release_mouse_button(LEFT_MOUSE_BUTTON)
        time.sleep(0.005)
        i += 1
        print(i)
elif input1 == "S" :
    input3 = int(input("Enter number of times cookie will be clicked"))
    input4 = input("Place your cursor on the cookie and press ENTER")
    while input3 != 0:
        press_mouse_button(LEFT_MOUSE_BUTTON)
        release_mouse_button(LEFT_MOUSE_BUTTON)
        input3 -= 1
        time.sleep(0.0005)
        print(input3)
if input3 == 0:
    print("DONE!")
    time.sleep(10)
    
    

    
