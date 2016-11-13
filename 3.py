import re
import urllib.request

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as response:
    text = response.read().decode('utf-8')

print("".join([c for c in re.findall('[^A-Z][A-Z]{3}([a-z])?[A-Z]{3}[^A-Z]', text) if c != '']) + '.html')
