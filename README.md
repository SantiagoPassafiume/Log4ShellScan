<h1 align="center">
  <br>
  Log4ShellScan
</h1>

<h3 align="center">This is a Python 3 Script that, given a list or file of urls, and a string to act as a server, will scan the provided urls for the "Log4Shell" (CVE-2021-44228) vulnerability.</h3>

## Download Log4ShellScan

```sh
    wget https://github.com/SantiagoPassafiume/Log4ShellScan.git
```

## Running Log4ShellScan

There are 2 ways of running this program

#### 1 - Standard way with python

```sh
    python3 Log4ShellScan.py <url_file> <server_string>
```

#### 2 - Without calling python directly

```sh
    chmod +x Log4ShellScan.py
    ./Log4ShellScan.py <url_file> <server_string>
```
