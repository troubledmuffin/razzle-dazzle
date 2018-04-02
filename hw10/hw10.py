import re
fname = input('Введите имя html- файла. ')
with open("file.txt", "w", encoding="utf-8") as f:
    with open (fname, "r", encoding="utf-8") as d:
        text = d.read()
    a = re.findall('<div class="">.*?Отряд.*?</td><td.*?><a.*?>(.*?)</a></td>', text) [0]
    f.write(a)





