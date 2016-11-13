import re
import urllib.request

# start nextNothing is 12345

nextNothing = '8022'
url = 'Nothing found'
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nextNothing
    with urllib.request.urlopen(url) as response:
        nextNothing = re.findall(r'and the next nothing is ([0-9]+)', response.read().decode('utf-8'))
    if nextNothing:
        nextNothing = nextNothing.pop()
    else:
        break

print(url)
