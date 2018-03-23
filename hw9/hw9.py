import re
fname=input('Enter file name: ')
def regfind():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
    a = re.findall('[Зз]агру[жз][иуяе][в]?[мтшлвн]?[иеа]?[ямйгуьенсо]?[усоыхю]?[ясагм]?[яьеихюйоу]?', text)
    print(a)
    
print(regfind())
