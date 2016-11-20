import re
import urllib.request

src = 'http://www.pythonchallenge.com/pc/def/'


with urllib.request.urlopen(src + 'hockey.html') as req:
    print(req.read())

print("Answer is \"OXYGEN\" - look in 6.py at letters")
