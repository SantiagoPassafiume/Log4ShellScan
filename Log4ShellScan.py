#!/bin/python3

# Title: Log4ShellScan
# Author: Santiago Passafiume
# License: MIT
# Github: https://github.com/SantiagoPassafiume
# Description: This script goes through a file containing urls and sends a GET request with the proper payload to each of them, checking if they're vulnerable to "Log4Shell" (CVE-2021-44228).


from urllib3 import disable_warnings
from sys import argv
from colorama import Fore
from utility import *


disable_warnings()


if __name__ == "__main__":
    try:
        counter = 0
        script_name = argv[0]
        url_file = argv[1]
        server_string = argv[2]
        urls = open_file(url_file)
        start_message()
        payload_sender(urls, server_string)
    except:
        print(
            f"""
{Fore.RED}Syntax: 

Option 1:
python3 Log4ShellScan.py <url_file> <server_string>


Option 2:
1 - chmod +x Log4ShellScan.py
2 - ./Log4ShellScan.py <url_file> <server_string>
"""
        )
