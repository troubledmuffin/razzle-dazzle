import re
i = 0
with open ("file2.txt","w", encoding = "utf-8") as d:
    with open ("mystem.xml","r", encoding = "utf-8") as f:
        text = f.read()
    a = re.findall('<.*?>\n<html><body>\n<se>(<w>.*</w>\n)</se>\n</body></html>', text) [0]
    for t in a:
        i+=1
    d.write(str(i))
##import re
##with open("file2.txt", "w", encoding="utf-8") as f:
##    with open ("mystem.xml", "r", encoding="utf-8") as d:
##        text = d.read()
##    a = re.findall('<.*?>\n<html><body><se>(.*?\n)</se>\n</body></html>', text) [0]
##    f.write(a)

               
