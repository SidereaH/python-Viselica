import random
import os
clear = lambda: os.system('cls')
print('Добро пожаловать на арену смерти 😈')

f1 = open('steps/1p.txt', encoding='utf-8')
f2 = open('steps/2p.txt', encoding='utf-8')
f3 = open('steps/3p.txt', encoding='utf-8')
f4 = open('steps/4p.txt', encoding='utf-8')
f5 = open('steps/5p.txt', encoding='utf-8')
f6 = open('steps/6p.txt', encoding='utf-8')
f7 = open('steps/7p.txt', encoding='utf-8')
f8 = open('steps/lastgg.txt', encoding='utf-8')
wordsfile = open('wordlist.txt', "r", encoding='utf-8')
wordlist = wordsfile.read()
word_into_list = wordlist.split("\n")

#words = ['человек', 'яблоко', 'русский', 'компьютер', 'вселенная', 'мозг', 'siderea', 'улица', 'перемотка']
countwordslist = len(word_into_list)
#print(countwordslist)
randomword = word_into_list[random.randint(0, countwordslist - 1)] #выбираем слово
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
        print(file)
    elif (countfails == 1):
        file = f2.read()
        print(file)
    elif (countfails == 2):
        file = f3.read()
        print(file)
    elif (countfails == 3):
        file = f4.read()
        print(file)
    elif (countfails == 4):
        file = f5.read()
        print(file)
    elif (countfails == 5):
        file = f6.read()
        print(file)
    elif (countfails == 6):
        file = f7.read()
        print(file)
    else:
        file = f8.read()
        print(file)
        print('Проигрыш (')
        break

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
    clear()
    if bottomlet.count('_') == False:
        print('Ура!!! Вы победили!!!')
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
        f7.close()
        f8.close()
        break