import os
import json

absolute_path = os.path.dirname(__file__)
full_path = os.path.join(absolute_path, 'book.txt')

f = open(full_path, 'r')
s = f.read()

book = json.loads(s)

print(book['bob'])
