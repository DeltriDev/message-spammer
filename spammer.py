from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
do = True
word = input("What would you like to spam?")
print("You have 3 seconds to swap to messanger app")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("SPAM!!!")

while do == True:
    keyboard.type(word)
    keyboard.press(Key.enter)
    time.sleep(1)
