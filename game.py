from slovar import five_letters
import random
import colorama
import time

colorama.init(autoreset=True)
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW

def begin():
    print("Добро пожаловать в игру WORDLE!")
    time.sleep(1.5)
    print("Суть игры заключается в том, чтобы угадать слово, состоящее из 5 букв")
    time.sleep(2)
    print(f"При вводе существующей в загаданном слове буквы она сменит свой цвет на {green + 'зеленый' }")
    time.sleep(2.5)
    print(f"Если буква в слове есть, но она находится не на своем месте, она будет иметь {yellow + 'желтый'} цвет")
    time.sleep(2.5)


def game():
    print("Итак, угадывайте слово! ")
    count = 0 
    score = 0 
    empty = ['_', '_', '_', '_', '_']
    empty2 = empty.copy()
    word = random.choice(five_letters)
    print(*empty)

    while True:
        print()
        letter = input("Введите букву >>> ").upper()
        mesto = input("Введите ее порядковый номер >>> ")
        print()
        if mesto.isdigit():
            mesto = int(mesto)
            if len(letter) == 1:
                if letter in word:
                    if word.count(letter) == 1: 
                            ind = word.find(letter)
                            if ind+1 == mesto:
                                print()
                                empty[ind] = green + letter
                                empty2[ind] = green + letter
                                print(*empty)
                                score += 1
                            
                            else:
                                print("Буква не на своем месте! ")
                                empty[mesto-1] = yellow + letter
                                empty2[mesto-1] = '_'
                                print(*empty)
                                empty = empty2.copy()
                                
                                

                    if word.count(letter) > 1:
                        for i in range(word.count(letter)):
                            ind = word.find(letter)
                            r_ind = word.rfind(letter)
                            if ind+1 == mesto:
                                empty[ind] = green + letter
                                empty2[ind] = green + letter
                                empty2[r_ind] = green + letter
                                print(*empty2)
                                empty = empty2.copy()
                                score += word.count(letter)
                                break
                            else:
                                print("Буква не на своем месте!")
                                print()
                                empty[mesto-1] = yellow + letter
                                empty2[mesto-1] = '_'
                                print(*empty)
                                break
                else:
                    print()
                    print("Такой буквы нет!")
                    count += 1
            else:
                print("Введите одну букву! ")
            
        else:
            print("Ошибка! При вводе порядкового номера введите цифру! ")

        scores(score, count, empty2, word)



def scores(score, count, empty2, word):
    if score == 5:
        print("Поздравляем! Вы угадали слово! Сыграть еще раз? >>> [Enter] | Выход >>> [1]")
        ans = input()
        if ans != '1':
            game()
        else:
            exit()
    elif count > 4:
        print(*empty2)
        print("Вы не угадали слово! Попробовать еще раз? >>> [Enter] | Выход >>> [1]")
        print("Загаданное слово:", word)
        ans = input()
        if ans != '1':
            game()
        else:
            exit()
            
begin()
s = input("Ну что, начинаем игру? >> [Enter] ")
game()
