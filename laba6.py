import random
import os
clear = lambda: os.system('cls')

fourdigit = 0
while len(set(str(fourdigit))) != 4:  
    fourdigit = random.randint(1000, 9999)


def same(data):
    for i in range(len(data)):
        j = i + 1
        while (j < len(data)):
            if (data[i] == data[j]):
                print('Введите уникальное 4-х значное число!')
                return False
            j += 1
    return True

def game():
    clear()
    print("Вы начали игру Быки и коровы!!!")
    print("Чтобы выиграть вам нужно угадать 4-х значное число!")
    print("Если вы угадаете число и оно будет на своем месте, вы получите быка!")
    print("Если вы угадаете число, но оно будет не на своем месте, вы получите корову!")
    print('Вводить нужно 4-х значное число с уникальными цифрами!')
    print("Для того чтобы выиграть вам нужно набрать 4 быка. Удачи!!!")
    bc = True
    numberattempts = 0
    while True:
        digituser = input("Введите число: ")
        four = str(fourdigit)
        digi = str(digituser)
        if len(digi) <= 3 or len(digi) > 4 :
            print("Введите 4-x значное число")
            os.system('pause')
            clear()
        if str(digituser) == str(fourdigit):
            print("Вы выиграли!")
            print("Это было число", fourdigit)
            print("Количество попыток:", numberattempts+1)  
            os.system('pause')
            mainmenu() 
        resultb = 0
        resultk = 0
        if len(digi) == 4 and same(digi):
            for i in range(len(four)): 
                if four[i] == digi[i]: 
                    resultb += 1
            for i in range(len(four)): 
                j = 0 
                while j < len(four): 
                    if digi[i] == four[j] and i != j: 
                        resultk += 1 
                    j += 1
            numberattempts += 1
            print("Количество быков:", resultb)
            print("Количество коров:", resultk)
    return

def mainmenu():
    mainm = 1
    while mainm:
        clear()
        print('БЫКИ И КОРОВЫ')
        print("Меню: ")
        print("1. Начать игру")
        print("2. Узнать загаданное число")
        print("3. Выход")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            game()
        if pick == 2:
            print('Загаданное число 4 - x значное число:', fourdigit)
            os.system('pause')
        elif pick == 3:
            mainm = 0
    return

mainmenu()