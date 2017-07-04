#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

BS = 32


def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s): return s[0:-s[-1]]


class AESCipher:

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt(self, raw):
        # raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        # return unpad(cipher.decrypt(enc[16:]))
        return cipher.decrypt(enc[16:])


aes = AESCipher('12345678')
encrypted = aes.encrypt('Secret Message A')
decrypted = aes.decrypt(encrypted)
print(encrypted)
print(decrypted)

'''
fix NoneModule issue
sudo pip3 uninstall Crypto
sudo pip3 uninstall pycrypto
sudo pip3 install pycrypto
'''