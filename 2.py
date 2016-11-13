import urllib.request
import re

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as resp:
    text = resp.read().decode('utf-8').split('<!--')

print("".join(re.findall(r'[a-z]', text[-1])))

