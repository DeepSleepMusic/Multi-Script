import random
import os as cmd
import colorama as color
import time
from tqdm import tqdm

print(color.Fore.LIGHTBLACK_EX + "Welcome To Auto Code Version 1. Made By: DeepSleepMusic")
time.sleep(0.1)

for i in tqdm (range (100), desc="Loading..."):
    pass
    time.sleep(0.1)

choice = input("""1: Password Generator\n2: Encyption Key/Create\n3: Decrypt File\n""")
password = ""
if choice == "1":
    max_val = 20
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "~!@#$%^&*()_+-=|\}]{[:;<>,./?"

    all = chars + lower_chars + numbers + symbols # Edit This To Edit Your Password.

    for index in range(max_val):
     password = password + random.choice(all)

print("Password Generated: {}".format(password))

if choice == "2":
    for i in tqdm (range (75), desc="Encrpyting File..."):
        pass
    time.sleep(0.2)
    print(cmd.system("cipher /e"))

    for i in tqdm (range (10), desc="Loading..."):
      pass
    time.sleep(0.6)
if choice == "3":
    print(cmd.system("cipher /d"))

    
