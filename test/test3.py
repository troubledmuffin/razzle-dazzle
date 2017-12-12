a = []
word=input('Enter word: ')
if word != '':
    a.append(word)
else:
    break
with open('Ozhegov.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        vocab = line.split('|')
        examp = vocab[1].split('||')
        for word in a:
            if word == vocab[0]:
                print(examp[1], '--', examp[0])
            else:
                print('Does not exist.')
