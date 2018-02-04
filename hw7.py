##какова частотность слов с приставкой omni- в тексте и частотность слов без приставки omni- (то есть, например, сообщает, сколько раз в тексте встречается слово omnibenevolent и сколько раз встречается слово benevolent, и так для всех слов с приставкой omni-)
import collections
fname=input('Enter file name: ')
def words_from_text(fname):
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    symbols="""(),.:;"'—«!?"""
    for s in symbols:
        text = text.replace(s, '')
    words = text.split()
    return words
def find_the_omnis(words):
    omnis = [ ]
    for word in words:
        if word.startswith('omni'):
            omnis.append(word)
    return omnis
def find_the_unomnis(words):
    unomnis = [ ]
    for word in words:
        if word[:4] == 'omni':
            new_word = word[4:]
            unomnis.append(new_word)
    return unomnis
def count_the_omnis(omnis):
    counter = collections.Counter(omnis)
    return counter
def count_the_unomnis(unomnis):
    c = collections.Counter(words)
    for o in unomnis:
        return c[o]
words = words_from_text(fname)
omnis = find_the_omnis(words)
unomnis = find_the_unomnis(words)
omnicount = count_the_omnis(omnis) 
unomnicount = count_the_unomnis(unomnis)
print("Words starting with omni-:", omnicount, "The same words but without the omni-:", unomnicount)


        
    


