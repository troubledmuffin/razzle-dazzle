with open('Ozhegov.txt', encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       vocab = line.split('|')
       words = vocab[0]
       a=[]
       i=0
       for word in words:
           if vocab[1] != '':
               a.append(word)
               i += 1
print(len(a))
print(i)
           
           
