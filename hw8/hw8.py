def dic():
    d = {}
    with open ('wordcombs.csv', encoding = 'utf-8') as f:
        text = f.readlines()
        for line in text:
            line = line.replace('\n', '')
            hint,word = line.split(';')
            d[hint] = word
        return d
def game(d):
    print('Не хотите ли сыграть в чрезвычайно увлекательную игру? Сейчас я загадаю вам слово. Ваша задача -- отгадать его с помощью подсказки. У вас три попытки! Поехали!')
    for h in d:
        print(h + '...')
        for i in range(5):
            guess = input('Ваша догадка: ')
            if guess == d[h]:
                print( 'Поздравляю, вы выиграли! Это было сложно, но вы справились! Я так горжусь вами!')
                break
            else:
                print( 'К сожалению, вы ошиблись. Попробуйте еще раз! ')
                if i == 0:
                    print( 'До лимита в 3 попытки 2 попытки.')
                if i == 1:
                    print( 'До лимита в 3 попытки 1 попытка.')
                
    print('Вот и подошла к концу наша игра. Вы не представляете, как приятно было провести с вами время! Даже если вы не отгадали ни одного слова, не расстраивайтесь! Жизнь состоит из побед и поражений, и если вас постигла неудача здесь, то наверняка повезет где-нибудь еще!'
)                
print(game(dic()))

