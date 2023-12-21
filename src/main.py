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


# TODO 1: Implement decrypt method stuff
def main() -> None:
    parser = argparse.ArgumentParser(description="Ramskit - CLI Tool for Ramskit")
    parser.add_argument('-a', '--action', dest="action", required=True,
                        help='Action to perform [encrypt/decrypt]')
    parser.add_argument('-p', '--path', dest="path", help='Path to file(s) to encrypt/decrypt')
    args = parser.parse_args()
    
    ramskit = Ramskit()
    key = ramskit.load_key()

    action = args.action.lower()
    encrypted = args.path

    # FIXME 3: Check args
    if action == 'encrypt':
        if not os.path.isfile(encrypted):
            print(f"[x] The file {encrypted} does not exist. Exiting...")
            sys.exit(1)

        if not encrypted:
            print("[x] Please provide the path to the file using the -p or --path option. Exiting...")
            sys.exit(1)

        ramskit.encrypt_file([encrypted], key)
        print("[x] File encrypted. Exiting...")

    elif action == 'decrypt':
        # FIXME 4: Check and fix key
        if not os.path.isfile(encrypted):
            print(f"[x] The file {encrypted} does not exist. Exiting...")
            sys.exit(1)

        if not encrypted:
            print("[x] Please provide the path to the file using the -p or --path option. Exiting...")
            sys.exit(1)

        ramskit.decrypt_file([encrypted], key)
        print("[x] File decrypted. Exiting...")

    else:
        if not action:
            print("[x] Please provide the action using the -a or --action option. Exiting...")
            sys.exit(1)
        else:
            print(f'[x] Invalid action: {action}. Exiting...')



if __name__ == '__main__':
    main()
    sys.exit(0)


