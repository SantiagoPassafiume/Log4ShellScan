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
        print(f"{Fore.LIGHTMAGENTA_EX}The scan has finished!")

    except:
        print(f"{Fore.RED}[!] Syntax: python3 {script_name} <url_file> <server_string>")
