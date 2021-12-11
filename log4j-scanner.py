#!/bin/python3

from sys import argv

import urllib3

from utility import *


urllib3.disable_warnings()


if __name__ == "__main__":
    try:
        counter = 0
        script_name = argv[0]
        url_file = argv[1]
        burp_colab_string = argv[2]
        urls = open_file(url_file)
        payload_sender(urls, burp_colab_string)
    except:
        print(
            f"[!] Syntax: python3 {script_name} <url_file> <server/burp_collaborator string>"
        )
