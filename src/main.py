#!/usr/bin/python3

""" Copyright (C) Luis De León

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

import cryptography
from cryptography import fernet

from ramskit import Ramskit
import os
import sys
import argparse

# I'm backkkkkkkk

# TODO: For v1.2.2 check logs for non-existent key
# TODO: For v1.3.1 ramskit package CLI init arg -> rather than main.py, use ramskit
# TODO: .deb package for v2.0.0 -> Also an apt package for Debian-based distros!
def main() -> None:
    # Typo docstring CLI help usages for v1.2.1
    """ Type 'python3 main.py -h (python main.py in Windows)' in console for help. """

    parser = argparse.ArgumentParser(description="Ramskit - CLI Usages")
    parser.add_argument('-a', '--action', dest="action", required=True,
                        help='Action to perform [encrypt/decrypt]')
    parser.add_argument('-p', '--path', dest="path", required=True,
                        help='Path to file(s) to encrypt/decrypt')
    args = parser.parse_args()
    
    ramskit = Ramskit()
    key = ramskit.load_key()

    action = args.action.lower()
    encrypted = args.path

    # Whole path needs to be checked in order to type action (encrypt/decrypt)
    if os.path.isfile(encrypted):
        if action == 'encrypt':
            if not encrypted:
                print("[x] Please provide the path to the file using the -p or --path option. ")

            directory = os.path.dirname(os.path.normpath(encrypted))
            notification_file_path = os.path.join(directory, 'look_at_me.txt')

            if os.path.exists(notification_file_path):
                print(f"[x] The file {encrypted} already encrypted. ")

            ramskit.encrypt_file([encrypted], key)
            print("[x] File encrypted. ")

        elif action == 'decrypt':
            try:
                if not encrypted:
                    print("[x] Please provide the path to the file using the -p or --path option. ")

                ramskit.decrypt_file([encrypted], key)
                print("[x] File decrypted. ")

            except cryptography.fernet.InvalidToken:
                print(f"[x] The file {encrypted} is not encrypted and doesn't have a key. ")

        else:
            if not action:
                print("[x] Please provide the action using the -a or --action option. ")

            print(f'[x] Invalid action: {action}. ')

    else:
        print(f"[x] The file {encrypted} does not exist. ")


# I usually add this stuff to every main.py haha
if __name__ == '__main__':
    main()  
    print("\n[x] Ramskit done. Exiting...")

    # I like this sys package, it closes ports :)
    sys.exit(0)


