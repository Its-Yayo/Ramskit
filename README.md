# Ramskit
Ramskit is a single ransomware tool to encrypt and decrypt data written in Python. Ramskit will automate wiich dir or file the user wants to encrypt and decrypt. Project still in tests.

## Usage

```bash
$ python3 ramskit.py -h
usage: ramskit.py [-h] -a ACTION -k KEY -p PATH

Ramskit - CLI Tool for Ramskit Ransomware

options:
  -h, --help            show this help message and exit
  -a ACTION, --action ACTION
                        Action to perform [encrypt/decrypt/generate_key]
  -k KEY, --key KEY     Key file
  -p PATH, --path PATH  Path to file(s) to encrypt/decrypt
```
## Pull Requests
You can test this project in your localhost by cloning it. 
```
$ git clone https://github.com/Its-Yayo/Ramskit.git
$ cd Keypwn
```

You can load in your localhost the last changes of Ramskit
```
$ git pull
```

This tool is just for educational and testing purposes. I'm not responsible of the damage a cracker would exponentially create. This project is under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.  

Happy coding folks. 
