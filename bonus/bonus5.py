word = input('Check out this amazing cypher! Write something: ')
aigy = ' '
cons = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
vowels = 'aAiIeEoOuU'
for character in word:
    if character == ' ':
        aigy += ' '
    else:
        for con in cons:
            if con == character:
                aigy += con+'aig'
        for v in vowels:
                if v == character:
                    aigy += v
print(aigy)
                
   
        
            
