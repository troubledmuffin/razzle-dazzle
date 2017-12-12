with open('Ozhegov.txt', encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       vocab = line.split('|')
       words = vocab[0]
       if len(words) >= 20:
           print(words)
           

