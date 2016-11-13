# Solve 1
ordA = ord('a')
ordZ = ord('z')
d = 2

s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
res = ''
for c in s:
    if (ord(c) >= ordA) and (ord(c) <= ordZ):
        if ord(c) + d <= ordZ:
            c = chr(ord(c) + d)
        else:
            c = chr(ordA + d - (ordZ - ord(c) + 1))
    res += c
print(res)

# Solve 2 in python 3.1
tr = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'cdefghijklmnopqrstuvwxyzab')
print('map'.translate(tr) + '.html')
