with open ("dom.txt", encoding = 'utf-8') as f:
    text = f.read()
a = 0
text = text.replace('\n', '')
text = text.replace('\xa0', '')
phrases  = text.split('. ')
print (phrases)
for phrase in phrases:
    symbols = """(-),:;"'—»«"""
    for s in symbols:
        phrase = phrase.replace(s, '')
##lensum = [a += len(i) for i in words]
    for i in phrase:
        print(i)
        print(len(i))
    a += len(i)
    print(a)
    avrg = [a / len(phrase) for phrase in phrases]
    if len(phrase) > 10:
        print('Это предложение со словами длины {}'.format(avrg))
    else:
        print('А это слишком корткое предложение!')

    
    

 
