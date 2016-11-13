import re
import urllib.request

nextNothing = '12345'
url = 'Nothing found'
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nextNothing
    with urllib.request.urlopen(url) as response:
        resp = response.read().decode('utf-8')
        if re.search(r'Divide by two', resp):
            nextNothing = str(int(nextNothing) / 2)
            continue
        nextNothing = re.findall(r'and the next nothing is ([0-9]+)', resp)
    if nextNothing:
        nextNothing = nextNothing.pop()
    else:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
            break
