with open ("dom.txt", encoding = 'utf-8') as f:
    text = f.read()

text = text.replace('\n', '')
text = text.replace('\xa0', '')
phrases  = text.split('. ')
print (phrases)
for phrase in phrases:
    symbols = """(-),:;"'—»«"""
    for s in symbols:
        phrase = phrase.replace(s, '')
    phrase = phrase.split()
    b = [len(i) for i in phrase]
    a = sum(b)
    avrg = a / len(phrase)
    if len(phrase) > 10:
        print('Это предложение со словами длины {:01.2f}'.format(avrg))
    else:
        print('А это слишком короткое предложение!')
    
    

 
