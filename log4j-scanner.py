#!/bin/python3
import urllib3
from sys import argv
from colorama import Fore
from utility import *


urllib3.disable_warnings()


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
            f"{Fore.RED}[!] Syntax: python3 {script_name} <url_file> <server/burp_collaborator string>"
        )
