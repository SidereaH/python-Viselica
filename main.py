import random
print('Добро пожаловать на арену смерти 😈')

f1 = open('steps/1p.txt', encoding='utf-8')
f2 = open('steps/2p.txt', encoding='utf-8')
f3 = open('steps/3p.txt', encoding='utf-8')
f4 = open('steps/4p.txt', encoding='utf-8')
f5 = open('steps/5p.txt', encoding='utf-8')
f6 = open('steps/6p.txt', encoding='utf-8')
f7 = open('steps/7p.txt', encoding='utf-8')
f8 = open('steps/lastgg.txt', encoding='utf-8')

words = ['человек', 'яблоко', 'русский', 'компьютер', 'вселенная']
countwordslist = len(words)
#print(countwordslist)
randomword = words[random.randint(0, countwordslist - 1)] #выбираем слово
countletter = len(randomword) #считаем буквы
bottomlet = []
gg = False
countfails = 0

for i in range(countletter):
    bottomlet.append('_')

bottomletstr =  '  '.join(bottomlet) #преобразование списка в строку
bottomletstr= bottomletstr.replace(' ', '') #удаление пробелов

while (gg == False):
    if(countfails == 0):
        file = f1.read()
    elif (countfails == 1):
        file = f2.read()
    elif (countfails == 2):
        file = f3.read()
    elif (countfails == 3):
        file = f4.read()
    elif (countfails == 4):
        file = f5.read()
    elif (countfails == 5):
        file = f6.read()
    elif (countfails == 6):
        file = f7.read()
    else:
        file = f8.read()
        print('Проигрыш (')
        break

    print("\033c", end="")

    print(file)
    print('Слово: ', bottomletstr)
    print('Ошибки: ', countfails)
    try:
        letter = input('Введите букву:' )
    except TypeError:
        print('Ошибка! Введите букву!')
    indexfound = randomword.find(letter)

    if(indexfound != -1):
        bottomlet.remove('_')
        bottomlet.insert(indexfound, letter)
        randomword = randomword.replace(letter, ' ', 1)
        bottomletstr = '  '.join(bottomlet)  # преобразование списка в строку
        bottomletstr = bottomletstr.replace(' ', '')  # удаление пробелов
    else:
        countfails = countfails + 1
    if bottomlet.count('_') == False:
        print('Ура!!! Вы победили!!!')
        break











