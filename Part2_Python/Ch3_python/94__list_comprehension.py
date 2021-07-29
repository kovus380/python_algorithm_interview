

import re

str1 = 'A3e3P3P2LENBA3AN2A'


strls = [
    str1[i:i+2].lower() for i in range(len(str1)-1)
    if re.findall('[a-z]{2,3}', str1[i:i+2].lower())
]


strls = []
for i in range(len(str1)-1):
    if re.findall('[a-z]{2,3}', str1[i:i+2].lower()):
        strls.append(str1[i:i+2].lower())
