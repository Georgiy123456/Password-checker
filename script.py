#**********************************************************
#Made by Georgiy Mintenko(Github profile:iamgeorgiy)      |
#09.01.2021                                               |
#Password checker                                         |
#**********************************************************
import os
from colorama import Fore, Back, Style
print(Fore.LIGHTBLUE_EX + "Hello,it's a script,in general:Password checker")
print(Fore.BLUE + Style.BRIGHT + "1.Password check\n2.Username check\n3.WiFi check")
option=int(input("Enter your option:"))
#password checker
if option == 1:
    name = str(input(Fore.GREEN + Style.DIM + "Enter the password: "))
    pwd = open('password.txt')  # opening passwords wordlist
    for line in pwd.read().rsplit():  # looping through passwords
        if name == line:
            print(Fore.CYAN + Style.BRIGHT + "Your Password " + name + " is Vulnerble")
            break
        else:
            print(
                "Ok,password not found in the merged database!")
            break
#username checker
if option == 2:
    name = str(input(Fore.GREEN + Style.DIM + "Enter the username: "))
    usr = open('usernames.txt')  # opening passwords wordlist
    for line in usr.read().rsplit():  # looping through passwords
        if name == line:
            print(Fore.CYAN + Style.BRIGHT + "Your username " + name + " is Vulnerble")
            break
        else:
            print(
                "Ok,password not found in the merged database!")
            break
#wifi passwoord checker
if option == 3:
   name = str(input(Fore.GREEN+"Enter the password: "))
   wifi = open('wifipwd.txt') #opening passwords wordlist
   for line in wifi.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your WiFi password "+name+" is Vulnerble")
           break
       else:
           print(
               "Ok,password not found in the merged database!")
           break
print(Fore.GREEN+"Thank You for Using this script!^_^")
