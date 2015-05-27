# спросить имя
# поздороваться
# выбрать время решения примеров
# выбрать режим
# загадать числа
# спросить результат сложения или вычитания
# проверить и огласить результат

import random

import time

name = input("Как тебя зовут? ")

print("Привет")

anstf = []

timelimit = input("Скажи, "+name+",сколько секунд тебе нужно для решения нескольких примеров:")

difficult = input("Выбери режим: сложение или вычитание? ")

while True:

        if difficult in ["сложение", "вычитание"]:
            break
        else:
            difficult = input("Просто выбери режим: ")

startTime = time.time()

questions = 0

answers = 0

num = 1

while True:

    number1 = random.randrange(1, 11)

    number2 = random.randrange(1, 11)

    if difficult == "сложение":
        guessStr = input(str(num)+"."+str(number1)+"+"+str(number2)+"=")
    
    if difficult == "вычитание":
        guessStr = input(str(num)+"."+str(number1)+"-"+str(number2)+"=")

    questions = questions+1

    num = num + 1

    while True:
        try:
            guess = int(guessStr)
        except:
            guessStr = input("Нужно ввести число а не ерунду! Введи заново: ")
        else:
            break
            
    if difficult == "сложение" and number1+number2==guess:
        answers = answers + 1
    elif difficult == "вычитание"and number1-number2==guess:
        answers = answers + 1

    if difficult == "сложение" and number1+number2==guess or difficult == "вычитание"and number1-number2==guess:
        anstf.append(True)
    else:
        anstf.append(False)

    timelimit = float(timelimit)    

    if time.time()-startTime > timelimit:
        print("Твой счёт"+" "+str(answers)+" "+"из"+" "+str(questions))
        for i in range(0, len(anstf)):
            if anstf[i] == True:
                print(str(i + 1) + ". Правильно")
            else:
                print(str(i + 1) + ". Неправильно")
        break

    print ("Осталось"+" "+str(int(timelimit-(time.time()-startTime)))+" "+"секунд")

