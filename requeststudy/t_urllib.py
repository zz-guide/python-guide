from urllib.request import urlopen


def func_main():
    func_urllib()
    pass


def func_urllib():
    url = 'http://worldtimeapi.org/api/timezone/etc/UTC.txt'
    with urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')  # Convert bytes to a str
            if line.startswith('datetime'):
                print(line.rstrip())  # Remove trailing newline
    pass
