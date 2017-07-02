#!/usr/bin/env python3


import getpass

from utils import util

count = 0

while count < 3:
    username = input("Enter User Name:")
    if isinstance(username, str):
        if username == "test":
            while count < 3:
                userpass = getpass.getpass(prompt="Enter your Password:")
                userpass = util.sha3512_with_salt('test', userpass)
                if userpass == "225c28ccb6cad0151a07d8745d9ad50d5426ed273a380" \
                               "4565ca07e5b729170fe175f145c87b8a3a3331f283824" \
                               "f964f664f2cb42478b561884ddde1a628e76b7098f6bc" \
                               "d4621d373cade4e832627b4f6":
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
