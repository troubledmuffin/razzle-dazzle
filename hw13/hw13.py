import os
import collections
a = {}
d = {}
i = 0
start_path = '.'
for root, dirs, files in os.walk(start_path):
    for di in dirs:
        for file in files:
            base, ext = os.path.splitext(file)
            folders = d.setdefault(di, {})
            files = folders.setdefault(file,{})
            ext = files.setdefault(ext)    
            counter = collections.Counter(files)
            print(counter)

            #это я не пытаюсь делать другой вариант, это мой, просто дальше этого момента, который у меня не получается тоже, я вообще не представляю, что делать, я в принципе не понимаю,как такую программу написать
