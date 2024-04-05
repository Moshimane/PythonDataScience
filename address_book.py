book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 my street, PLK',
    'phone': 123456789
}

book['bob'] = {
    'name': 'bob',
    'address': '1 his street, PLK',
    'phone': 123456780
}

import json
import os
s = json.dumps(book)
print(s)

absolute_path = os.path.dirname(__file__)
full_path = os.path.join(absolute_path, 'book.txt')
#use with to avoid closing the file - files closes automatically
with open(full_path, 'w') as f: #w = write and a=append and r=read and r+=read+write(doesn't create file if it doesn't exist) and w+=write+read(creates file if it doesn't exist)
   f.write(s)