import os
import re
import csv
import collections
def task1():
    path = 'news'
    for fname in os.listdir(path):
        file = os.path.join(path, fname)
        with open (file, encoding = 'windows-1251', errors = 'ignore') as f:
            lines = f.readlines()
        for line in lines:
            a = re.findall('name="(\w+)', line)
            b = re.findall('content="(\w+)', line)
            for i in a:
                if i in line:
                    print(i, ',', b)
def task2():
    path = 'news'
    for fname in os.listdir(path):
       file = os.path.join(path, fname)
       with open (file, encoding="windows-1251", errors='ignore') as f:
            text = f.read()
            a = re.findall(r'lex="[А-Я]+"', text)
            c = collections.Counter(a)
            print(c)
print(task1())
print(task2())
