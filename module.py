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
    

def loose(randwin):
    print('Вы проиграли')
    print('Слово: ', randwin)


def questcont():
    a = input('Еще раз? y/n')
    a.lower()
    if a == 'y':
        again = True
    else:
        again = False
    return again


    
    
def wordAndErrors(bottomletstr, countfails, descr):
    print('Описание: ', descr)
    print('Слово: ', bottomletstr)
    print('Ошибки: ', countfails)
    
def inputletter():
    try:
        letterr = input('Введите букву:' )
        if letterr.isupper():
            letterr.lower()
    except TypeError:
        print('Ошибка! Введите букву!')
    
    return letterr
def searchFor(bottomlet, letter, indexfound, randomword, bottomletstr):
    bottomlet.remove('_')
    bottomlet.insert(indexfound, letter)
    randomword = randomword.replace(letter, ' ', 1)
    bottomletstr = '  '.join(bottomlet)  # преобразование списка в строку
    bottomletstr = bottomletstr.replace(' ', '')  # удаление пробелов
def winGame(randwin):
    randwin.upper()
    print('Ура!!! Вы победили!!!')
    print("Слово:", randwin)
def counterr(countfails):
    countfails = countfails + 1
    return countfails
def worddict(): #создание словаря из файла
    with open('dictwordlist.txt') as file:  # Читаем файл
        lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк

    dic = {}  # Создаем пустой словарь

    for line in lines:  # Проходимся по каждой строчке
        key, value = line.split(': ')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
        dic.update({key: value})  # Добавляем в словарь

    return dic  # возвращение слооваря
def randomdictkey(worddictl):
    wordfrdict, descript = random.choice(list(worddictl.items()))
    return wordfrdict, descript
def emptyDictionary(dictionary):
    if bool(dictionary) == False:
        print("Поздравляю, у нас закончились слова")
        fullgg = True
    else:
        fullgg = False
    return fullgg
