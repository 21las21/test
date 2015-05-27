# спросить имя
# поздороваться
# загадать числа
# спросить результат сложения
# проверить и огласить результат

import random

number1 = random.randrange(1, 11)

number2 = random.randrange(1, 11)

guess = input(str(number1)+"+"+str(number2)+"=")

while True:

    guess = int(guess)

    if guess == number1+number2:
        print("Молодец! Ты угадал!")
        break
    else:
        guess = input("Неудача. Попробуй ещё. ")

