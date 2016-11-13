import re
import pickle
import urllib.request

src = 'http://www.pythonchallenge.com/pc/def/'
with urllib.request.urlopen(src + 'peak.html') as response:
    pickleSrc = re.findall(r'<peakhell src="(.+)"/>', response.read().decode('utf-8'))
    if pickleSrc:
        with urllib.request.urlopen(src + pickleSrc.pop()) as response:
            for data in pickle.loads(response.read()):
                print(''.join([d[0]*d[1] for d in data]))
