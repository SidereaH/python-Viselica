import random
import module
module.clear()
#print('Добро пожаловать на арену смерти 😈')


randomword = module.wordslib('wordlist.txt')
randwin = randomword
countletter = countletter = len(randomword)
bottomlet = []
gg = False
countfails = 0

for i in range(countletter):
    bottomlet.append('_')

bottomletstr =  '  '.join(bottomlet) #преобразование списка в строку
bottomletstr= bottomletstr.replace(' ', '') #удаление пробелов

while (gg == False):
    if(countfails == 0):
        module.workwthFile('steps/1p.txt')
    elif (countfails == 1):
        module.workwthFile('steps/2p.txt')
    elif (countfails == 2):
        module.workwthFile('steps/3p.txt')
    elif (countfails == 3):
        module.workwthFile('steps/4p.txt')
    elif (countfails == 4):
        module.workwthFile('steps/5p.txt')
    elif (countfails == 5):
        module.workwthFile('steps/6p.txt')
    elif (countfails == 6):
        module.workwthFile('steps/7p.txt')
    else:
        module.workwthFile('steps/lastgg.txt')
        module.loose(randwin)
        #print('Проигрыш (')
        break
    module.wordAndErrors(bottomletstr, countfails)
    
    letter = module.inputletter()
    
    indexfound = randomword.find(letter)
    if letter == randwin:
        module.winGame(randwin)
        break
    if(indexfound != -1):
        #module.searchFor(bottomlet, letter, indexfound, randomword, bottomletstr)
        bottomlet.remove('_')
        bottomlet.insert(indexfound, letter)
        randomword = randomword.replace(letter, ' ', 1)
        bottomletstr = '  '.join(bottomlet)  # преобразование списка в строку
        bottomletstr = bottomletstr.replace(' ', '')  # удаление пробелов
    else:
        countfails = module.counterr(countfails)
    module.clear()
    if bottomlet.count('_') == False:

        module.winGame(randwin)
        break
