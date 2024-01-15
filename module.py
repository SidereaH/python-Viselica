import os
import random
def clear():
    clearcon = lambda: os.system('cls')
    clearcon()
def wordslib(wordlibpath):
    wordsfile = open(wordlibpath, "r", encoding='utf-8')
    wordlist = wordsfile.read()
    word_into_list = wordlist.split("\n")

#words = ['человек', 'яблоко', 'русский', 'компьютер', 'вселенная', 'мозг', 'siderea', 'улица', 'перемотка']
    countwordslist = len(word_into_list)
#print(countwordslist)
    randomword1 = word_into_list[random.randint(0, countwordslist - 1)] #выбираем слово
    return randomword1

    
def workwthFile(file):
    f1 = open(file, encoding='utf-8')
    file = f1.read()
    print(file)
    f1.close()
    

def loose():
    print('Вы проиграли')
    
    
def wordAndErrors(bottomletstr, countfails):
    print('Слово: ', bottomletstr)
    print('Ошибки: ', countfails)
    
def inputletter():
    try:
        letterr = input('Введите букву:' )
    except TypeError:
        print('Ошибка! Введите букву!')
    
    return letterr
def searchFor(bottomlet, letter, indexfound, randomword, bottomletstr):
    bottomlet.remove('_')
    bottomlet.insert(indexfound, letter)
    randomword = randomword.replace(letter, ' ', 1)
    bottomletstr = '  '.join(bottomlet)  # преобразование списка в строку
    bottomletstr = bottomletstr.replace(' ', '')  # удаление пробелов
def winGame():
    print('Ура!!! Вы победили!!!')