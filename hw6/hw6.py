
import random
def masc_noun():
    with open ('m_nouns.txt', encoding = 'utf-8') as f:
        m_nouns = f.readlines()
    return 'le' + ' ' + random.choice(m_nouns)
def plur_noun():
    with open ('p_nouns.txt', encoding = 'utf-8') as f:
        p_nouns = f.readlines()
    return 'les' + ' ' + random.choice(p_nouns)
def sing_adj(noun):
    with open ('s_adj.txt', encoding = 'utf-8') as f:
        s_adj = f.readlines()
    result = noun + ' ' + random.choice(s_adj)
    return result
def plur_adj(noun):
    with open ('plur_adj.txt', encoding = 'utf-8') as f:
        plur_adj = f.readlines()
    result = noun + ' ' + random.choice(plur_adj)
    return result
def verb (suj, obj):
    with open ('verbs.txt', encoding = 'utf-8') as f:
 #       f = f.replace(" ", "")
        verbs = f.readlines()
    result = suj + ' ' + random.choice(verbs) + ' ' + obj
    return result
def neg_verb (suj, obj):
    with open ('verbs.txt', encoding = 'utf-8') as f:
        verbs = f.readlines()
    random_verb = random.choice(verbs)
    vowels = ['a','o','e','é','i']
    
    if random_verb[0] in vowels:
        result = suj + ' ' + "n'" + random_verb + ' ' + 'pas' + ' ' + obj
    else:
        result = suj + ' ' + "ne" + ' ' + random_verb + ' ' + 'pas' + ' ' + obj
    return result
def rand_sent_pos():
    result = verb(masc_noun(),plur_adj(plur_noun())) + '.'
    return result
def rand_sent_if():
    result = verb(masc_noun(),plur_adj(plur_noun())) + ', ' + 'si' + ' ' + neg_verb(masc_noun(),plur_adj(plur_noun()))  + '.'
    return result
def rand_sent_neg():
    result = neg_verb(masc_noun(),plur_adj(plur_noun())) + '.'
    return result
def rand_sent_interro():
    result = 'est-ce que' + ' ' + verb(masc_noun(),plur_adj(plur_noun())) + '?'
    return result
def rand_sent_imper():
    result = verb("",plur_noun()) +  '!'
    result = result[1:]
    return result
def abs_rand():
    sent = random.choice([1,2,3,4,5])
    if sent == 1:
        return rand_sent_pos()
    elif sent == 2:
        return rand_sent_neg()
    elif sent == 3:
        return rand_sent_interro()
    elif sent == 4:
        return rand_sent_imper()
    elif sent == 5:
        return rand_sent_if()
for i in range(5):
    phrase = abs_rand()
    phrase = phrase.capitalize()
    phrase = phrase.replace('\n', '')
    print(phrase)
    
