# password-manager
A password manager written in Python

Modules used:
os, base64, hashlib, Crypto

This app will use a user-defined master password to encrypt a CSV file using AES 256 and write all the users passwords to a custom .ep (encrypted passwords) file. This file can later be decrypted using the master password.
