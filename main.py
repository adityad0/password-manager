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
PASSWORDS_FILE_NAME = "passwords.passdata"
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

def show_brand():
    print(Style.RESET_ALL)
    print(Fore.RED + " _____       "+Fore.BLUE+" _____  __  __ "+Fore.WHITE+"        "+Fore.YELLOW+" ___ "+Fore.GREEN+"  ____       _         "+Fore.YELLOW+" ___ ")
    print(Fore.RED + "|  __ \      "+Fore.BLUE+"|  __ \|  \/  |"+Fore.WHITE+"        "+Fore.YELLOW+"|  _|"+Fore.GREEN+" |  _ \     | |        "+Fore.YELLOW+"|_  |")
    print(Fore.RED + "| |__) |   _ "+Fore.BLUE+"| |__) | \  / |"+Fore.WHITE+"  ____  "+Fore.YELLOW+"| |  "+Fore.GREEN+" | |_) | ___| |_ __ _  "+Fore.YELLOW+"  | |")
    print(Fore.RED + "|  ___/ | | |"+Fore.BLUE+"|  ___/| |\/| |"+Fore.WHITE+" |____| "+Fore.YELLOW+"| |  "+Fore.GREEN+" |  _ < / _ \ __/ _` | "+Fore.YELLOW+"  | |")
    print(Fore.RED + "| |   | |_| |"+Fore.BLUE+"| |    | |  | |"+Fore.WHITE+"        "+Fore.YELLOW+"| |  "+Fore.GREEN+" | |_) |  __/ || (_| | "+Fore.YELLOW+"  | |")
    print(Fore.RED + "|_|    \__, |"+Fore.BLUE+"|_|    |_|  |_|"+Fore.WHITE+"        "+Fore.YELLOW+"| |_ "+Fore.GREEN+" |____/ \___|\__\__,_| "+Fore.YELLOW+" _| |")
    print(Fore.RED + "        __/ |"+Fore.BLUE+"               "+Fore.WHITE+"        "+Fore.YELLOW+"|___|"+Fore.GREEN+"                       "+Fore.YELLOW+"|___|")
    print(Fore.RED + "       |___/ ")
    print(Style.RESET_ALL)

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
    master_password_input = getpass(Fore.BLUE + "Enter master password: " + Style.RESET_ALL)
    master_password_input_hash = hashlib.sha512(master_password_input.encode()).hexdigest()
    MASTER_PASSWORD = master_password_input
    if str(master_password_input_hash) == str(master_password_hash):
        return True
    else:
        return False

def get_passwords_list(passwords_file_read):
    passwords_list = []
    with passwords_file_read as file:
        while (line := file.readline().rstrip()):
            passwords_list.append(line)
    line_num = 0
    for indv_line in passwords_list:
        passwords_list[line_num] = indv_line.split(",")
        line_num += 1

    return passwords_list

# DECRYPTED_PASSWORDS = [['https://lynkr.org/', ' lynkr', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://google.com/', 'google', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://microsoft.com/', 'microsoft', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://amazon.com/', 'amazon', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://ebay.com/', 'ebay', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://facebook.com/', 'facebook', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://instagram.com/', 'instagram', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://twitter.com/', 'twitter', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456'], ['https://spotify.com/', 'spotify', 'adityad@att.net', ' password!1234', '2001-12-12 12:12:12.123456']]

def search_login(app_name):
    global DECRYPTED_PASSWORDS
    search_results = []
    for indv_login in DECRYPTED_PASSWORDS:
        if indv_login[1].find(app_name) == -1:
            continue
        else:
            search_results.append(indv_login)
    return search_results

def save_new_login():
    pass

def menu():
    show_brand()
    print(Fore.YELLOW + "Python Password Manager V1.0 [BETA]" + Style.RESET_ALL)
    print()
    print(Fore.YELLOW + "1. " + Style.BRIGHT + "Search login" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. " + Style.BRIGHT + "Save new login" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. " + Style.BRIGHT + "Update a saved password" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. " + Style.BRIGHT + "View all logins" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. " + Style.BRIGHT + "Change master password" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. " + Style.BRIGHT + "Quit" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. " + Style.BRIGHT + "Destroy all passwords [ ! USE WITH CAUTION ! ]" + Style.RESET_ALL)
    print()
    opt = input(Fore.YELLOW + "Option: " + Style.BRIGHT)
    if checkIfInt(opt):
        opt = int(opt)
        if opt == 1:
            print()
            app_name = input(Style.RESET_ALL + Fore.YELLOW + "App/Website name: " + Style.RESET_ALL)
            search_results = search_login(app_name)
            if len(search_results) > 0:
                print()
                print(Fore.YELLOW + "Search results for \""+Style.RESET_ALL+app_name+Fore.YELLOW+"\":")
                print(Style.RESET_ALL)
                search_results = search_results[0]
                print(Style.BRIGHT + Fore.YELLOW + "Website URL:     " + Style.RESET_ALL + search_results[0])
                print(Style.BRIGHT + Fore.YELLOW + "Website Name:   " + Style.RESET_ALL + search_results[1])
                print(Style.BRIGHT + Fore.YELLOW + "Username:        " + Style.RESET_ALL + search_results[2])
                print(Style.BRIGHT + Fore.YELLOW + "Password:       " + Style.RESET_ALL + search_results[3])
                print(Style.BRIGHT + Fore.YELLOW + "Saved on:        " + Style.RESET_ALL + search_results[4])
                print()
                input(Fore.YELLOW + "Press enter/return to return to the menu.." + Style.RESET_ALL)
                clscr()
                menu()
        elif opt == 2:
            save_new_login()
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt == 6:
            clscr()
            show_brand()
            print(Fore.GREEN+"Application closed.")
            print()
            quit()
        elif opt == 7:
            pass
        else:
            clscr()
            print(Fore.RED +"Invalid Option." + Style.RESET_ALL)
            menu()
    else:
        clscr()
        print(Fore.RED +"Invalid Option." + Style.RESET_ALL)
        menu()

def main():
    global DECRYPTED_PASSWORDS
    if validate_master_password(get_master_password_hash()):
        passwords_file_read = get_passwords_file_read()
        DECRYPTED_PASSWORDS = get_passwords_list(passwords_file_read)
        passwords_file_write = get_passwords_file_write()
        passwords_file_read.close()
        passwords_file_write.close()
        clscr()
        menu()
    else:
        clscr()
        show_brand()
        print(Fore.RED + "Invalid master password!" + Style.RESET_ALL)
        main()

# password@1234

try:
    if __name__ == '__main__':
        clscr()
        show_brand()
        main()
except KeyboardInterrupt:
    clscr()
    print(Fore.RED + "Application forcefully closed!")
    quit()