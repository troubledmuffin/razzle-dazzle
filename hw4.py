with open("text.txt", encoding = "utf-8") as f:
    text = f.read()
text = text.replace (".", "")
text = text.replace (",", "")
text = text.replace ("–", "")
words = text.split()
i = 0
capitals = "А Б В Г Д Е Ё Ж З И К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я"
for word in words:
    for capital in capitals:
        if word.startswith(capital):
            i += 1
percentage = i / len(words) * 100
print("Процент слов, начинающихся с загланой буквы, равен", percentage)

            
        
