import re
with open("file.txt", "w", encoding="utf-8") as f:
    with open ("fin.html", "r", encoding="utf-8") as d:
        text = d.read()
    a = re.sub(r'Финл[я|я́]нди', 'Малайзи', text) 
    f.write(a)
