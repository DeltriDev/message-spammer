import time
import os

try:
    import pynput
except ImportError:
    input(f"Module pynput not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install pynput'\nPress enter to exit")
    exit()
from pynput.keyboard import Key, Controller

keyboard = Controller()
do = True
print("Made by SamAlexandros#2211 (TacoSuaceDev)")
time.sleep(1)
print("")
word = input("What would you like to spam? ")
print("Spam starts in:")
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
