#!/usr/bin/env python


import getpass

count = 0

while count < 3:
    username = input("Enter User Name:")
    if username is str:
        if username == "test":
            while count < 3:
                userpass = getpass.getpass(prompt="Enter your Password:")
                if userpass == "art2cat":
                    print("User:", username, ", login successful!")
                    break
                else:
                    count += 1
                    if count != 3:
                        print("Login failed", count)
                    else:
                        print("The maximum number of login!")
            break
        else:
            count += 1
            if count != 3:
                print("Username incorrect!")
            else:
                print("The maximum number of login!")
    else:
        count += 1
        if count != 3:
            print("Username must be string!")
        else:
            print("The maximum number of login!")
