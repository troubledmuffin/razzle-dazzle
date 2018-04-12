import re
with open ("file3.txt", "w", encoding = 'utf-8') as d:
    with open ("mystem.xml", encoding = 'utf-8') as f:
        text = f.read()
    d = {}
    i = 0
    a = re.findall('<ana>.*?gr="(.*?)"/>', text) [0]
    for l in a:
        i+=1
    d[i]=a
    f.write(d[a], ':', d[i] + '\n')
        
    
