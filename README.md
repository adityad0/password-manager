# password-manager
A password manager written in Python

Modules used:
The following modules must be installed to use the app unless it has been compiled to an EXE: os, platform (platform), datetime, hashlib, re, csv, colorama (init, Fore, Back, Style) and getpass. The msvcrt module will be imported only if the app is running on a Windows device.

os - To run shell scripts which will hide the password files
platform - To identify the OS type.
datetime - Get the current system date and time
hashlib - (Currently unused)
re - To compare regex
csv - To parse and store all the passwords after they are encrypted
colorama - To add some colors!
getpass - To hide the password input on the terminal.

This app will use a user-defined master password to encrypt a CSV file using AES 256 and write all the users passwords to a custom .ep (encrypted passwords) file. This file can later be decrypted using the master password.

The app relies on a master password which will be stored in the master_password.key file after the password has been encrypted with SHA256 (No salt used). All passwords will be AES encrypted and stored in the passwords.csv.

FEATURES I'M PLANNING ON ADDING:
1. Ability to store documents like passports, and other ID cards.


This app is still in the BETA phase and not work as intended. DO NOT USE THIS APP TO STORE YOUR PASSWORDS FOR ANY WEBSITE/APPLICATION AS IT IS STILL UNDER DEVELOPMENT. THE AUTHOR(S) / DEVELOPER(S) OF THIS APP ARE NOT RESPONSIBLE FOR ANY DATALOSS, DAMAGE TO THEFT OF YOUR PASSWORDS.

This app was written from scratch by Aditya Desai.
