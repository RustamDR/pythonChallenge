import re
import urllib.request
import zipfile

src = 'http://www.pythonchallenge.com/pc/def/channel.zip'
zipFileName = ''.join('downloads/' + src.split('/')[-1])
urllib.request.urlretrieve(src, zipFileName)

with zipfile.ZipFile(zipFileName, 'r') as zipFile:
    file, comments = '%s.txt', []
    fileNum = 'readme'
    while True:
        comments.append(zipFile.getinfo(file % fileNum).comment.decode('utf-8'))
        fileNum = re.findall(r'\s(\d+)', str(zipFile.read(file % fileNum)))
        if not fileNum:
            break
        fileNum = fileNum.pop()
    print(''.join(comments))
