#!/usr/bin/python3
try:
    import os
    from platform import system
    import datetime
    import hashlib
    import re
    import csv
    from colorama import init, Fore, Back, Style
    from getpass import getpass
except ModuleNotFoundError:
    print("One or more modules could not be imported.")

init()

opr_sys = system()
if opr_sys == "Linux":
    opr_sys = "l"
elif opr_sys == "Windows":
    opr_sys = "w"

cwd = os.getcwd()
current_date_time = datetime.datetime.now()
MASTER_PASSWORD_FILE_NAME = "master_password.key"
PASSWORDS_FILE_NAME = "passwords.csv"
MASTER_PASSWORD = ''
DECRYPTED_PASSWORDS = ''

# Declare custom errors
class baseError(Exception):
    pass
class masterPasswordLenError(baseError):
    pass

def checkIfInt(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False

def clscr():
    if opr_sys == 'w':
        os.system('cls')
    else:
        os.system('clear')

# Get the password file
def get_passwords_file_read():
    try:
        passwords_file_read = open(PASSWORDS_FILE_NAME, "r")
    except FileNotFoundError:
        passwords_file_read = open(PASSWORDS_FILE_NAME, "w+")
        passwords_file_read = open(PASSWORDS_FILE_NAME, "r")
    return passwords_file_read

def get_passwords_file_write():
    try:
        passwords_file_write = open(PASSWORDS_FILE_NAME, "a")
    except FileNotFoundError:
        passwords_file_write = open(PASSWORDS_FILE_NAME, "w+")
        passwords_file_write = open(PASSWORDS_FILE_NAME, "w")
    return passwords_file_write

def set_master_password():
    master_password = input("Enter a master password: ")
    # Validate the password input
    # test master password = Password@1234
    if len(master_password) > 8 and len(master_password) < 24:
        if re.match(r"([A-Za-z0-9!@#$%^*)(\-_+=\{\}\[\]<>?/~])\w+", master_password):
            clscr()
            # The master password is strong enough. Save the master password hash in the file
            master_password_hash = hashlib.sha512(master_password.encode()).hexdigest()
            master_password_file = open(MASTER_PASSWORD_FILE_NAME, 'w+')
            master_password_file.write(master_password_hash)
            master_password_file.close()
            print("Master password set.")
            return master_password_hash
        else:
            clscr()
            print("Master password is not strong enough!")
            set_master_password()
    else:
        clscr()
        print("Master password must be over 8 and under 24 characters in length!")
        set_master_password()

def get_master_password_hash():
    try:
        master_password_file = open(MASTER_PASSWORD_FILE_NAME, "r")
        master_password_hash = master_password_file.readline()
        master_password_file.close()
    except FileNotFoundError:
        master_password_hash = set_master_password()
    return master_password_hash

def validate_master_password(master_password_hash):
    global MASTER_PASSWORD
    master_password_input = getpass("Enter master password: ")
    master_password_input_hash = hashlib.sha512(master_password_input.encode()).hexdigest()
    MASTER_PASSWORD = master_password_input
    if str(master_password_input_hash) == str(master_password_hash):
        return True
    else:
        clscr()
        print(Fore.RED + "Invalid password!" + Style.RESET_ALL)
        validate_master_password(master_password_hash)

def read_passwords(passwords_file_read):
    # with passwords_file_read as pass_file:
    #     reader = csv.reader(pass_file, delimiter=' ', quotechar='|')
    #     passwords_list = []
    #     for row in reader:
    #         passwords_list = passwords_list + row
    #         print(passwords_list)
    lines = passwords_file_read.readlines()
    return lines

read_passwords(open('passwords.csv', 'r'))
quit()

def menu():
    print(Fore.YELLOW + "Python Password Manager V1.0 [BETA]" + Style.RESET_ALL)
    print()
    print("1. Search login")
    print("2. Save new login")
    print("3. Update a saved password")
    print("4. View all logins")
    print("5. Change master password")
    print("6. Quit")
    print("7. Destroy all passwords [! CAREFUL WITH THIS !]")
    print()
    opt = input("Option: ")
    if checkIfInt(opt):
        opt = int(opt)
        if opt == 1:
            pass
        elif opt == 2:
            pass
        else:
            pass
    else:
        pass

def main():
    # Check the master password
    master_password_hash = get_master_password_hash()
    if validate_master_password(master_password_hash):
        clscr()
        menu()
    else:
        print("Invalid master password!")
        quit()

    passwords_file_read = get_passwords_file_read()
    print(read_passwords(passwords_file_read))
    passwords_file_write = get_passwords_file_write()
    passwords = passwords_file_read.read()

    # passwords_file_write.write(str(test_passwords_data) + "\n")

    print(passwords)

    passwords_file_read.close()
    passwords_file_write.close()


if __name__ == '__main__':
    clscr()
    main()