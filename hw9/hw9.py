import re
fname=input('Enter file name: ')
def regfind():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
    a = re.findall(r'\b[Зз]агру[жз][иуяе][в]?[мтшлвн]?[иеа]?[ямйгуьенсо]?[усоыхю]?[ясагм]?[яьеихюйоу]?\b', text)
    print(a)
    
print(regfind())
